from string import Template
import json
import random
import time
import copy

import pygit

commit_interval = 60 #seconds - used to calculate bar width for chart

with open('series.html') as fh:
    template = fh.read()

with open('place.html') as fh:
    placeholder = fh.read()

with open('graph.js') as fh:
    graph_js = fh.read()

placeholders = ''
graphs = ''

for num in range(3):
    s = Template(placeholder)
    placeholders += s.safe_substitute(num=num)

    max_lines = 0
    line_data = []
    syntax_data = []
    git_data = pygit.parse_git('./work','ttest.py')
    for entry in git_data:
        line_data.append([entry['time'],entry['lines']])
        if entry['lines'] > max_lines:
            max_lines = entry['lines']
        syntax_data.append([entry['time'],entry['syntax']])

    #interpolate time
    first = True
    interpolated_syntax_data = []
    for entry in syntax_data:
        if not first:
            for time in range(last_entry[0]+1000,entry[0],1000):
                new_entry = [time,last_entry[1]]
                interpolated_syntax_data.append(new_entry)
            

        interpolated_syntax_data.append(entry)
        last_entry = entry
        first = False

        
    syntax_data = interpolated_syntax_data

    #normalise against lines
    for entry in syntax_data:
        entry[1]*= max_lines

    s = Template(graph_js)
    graphs += s.safe_substitute(num=num,
        syntax_data=json.dumps(syntax_data),
        line_data=json.dumps(line_data),
        bar_width=1000)

with open('op.html','w') as html:
    s = Template(template)
    html.write(s.safe_substitute(javascript=graphs,placeholders=placeholders))

