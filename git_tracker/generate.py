from string import Template
import json
import random
import time
import copy
from config import *
import pygit


with open('series.html') as fh:
    template = fh.read()

with open('place.html') as fh:
    placeholder = fh.read()

with open('graph.js') as fh:
    graph_js = fh.read()

placeholders = ''
graphs = ''

files=[]
git_data = pygit.fetch_git(local_dir)
for file in git_data:
    if file["name"] not in files:
        files.append(file["name"])
file_num = 0
min_time = time.time() * 1000
max_lines = 0
for file in files:
    print(file)
    s = Template(placeholder)
    placeholders += s.safe_substitute({'num':file_num,'file':file})

    line_data = []
    syntax_data = []
    for entry in git_data:
        if entry["name"] != file:
            continue

        print(entry)
        line_data.append([entry['time'],entry['lines']])
        if entry['time'] < min_time:
            min_time = entry['time']

        if entry['lines'] > max_lines:
            max_lines = entry['lines']

        if entry['syntax']:
            syntax = 1
        else:
            syntax = 0
        syntax_data.append([entry['time'],syntax])

    #interpolate time
    first = True
    interpolated_syntax_data = []
    for entry in syntax_data:
        if not first:
            for itime in range(last_entry[0]+time_res,entry[0],time_res):
                new_entry = [itime,last_entry[1]]
                interpolated_syntax_data.append(new_entry)
            

        interpolated_syntax_data.append(entry)
        last_entry = entry
        first = False
    #need to continue values until now
    
        
    syntax_data = interpolated_syntax_data

    s = Template(graph_js)
    graphs += s.safe_substitute({'num':file_num,
        'syntax_data':json.dumps(syntax_data),
        'line_data':json.dumps(line_data),
        'bar_width':time_res})

    file_num += 1

with open('op.html','w') as html:
    s = Template(template)
    html.write(s.safe_substitute(
        {
            'javascript':graphs,
            'placeholders':placeholders,
            'min_time': "%d" % (min_time),
            'max_time': "%d" % (time.time() * 1000),
            'max_lines': max_lines * 1.1,
        }))
    print min_time
    print time.time() * 1000
