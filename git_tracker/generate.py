#!/usr/bin/python
from string import Template
import json
import pprint
import time
import copy
from config import *
import git_wrapper

pp = pprint.PrettyPrinter()

with open('template.html') as fh:
    template = fh.read()

with open('place.html') as fh:
    placeholder = fh.read()

with open('graph.js') as fh:
    graph_js = fh.read()

#globals
placeholders = ''
graphs = ''
file_num = 0
files=[]

#fetch details for each user from the repo
users = git_wrapper.fetch_git(local_dir)

#process each user
for user in users.get_users():
    if verbose:
        print(user.name)

    s = Template(placeholder)
    placeholders += s.safe_substitute(
        {
            'num':file_num,
            'link':user.get_path(),
            'link_name':user.get_link(),
        })

    #process history
    line_data = []
    syntax_data = []
    for entry in user.get_history():
        if verbose:
            entry.pprint()
        line_data.append([entry.time,entry.lines])
        syntax_data.append([entry.time,entry.syntax])
    
    #need to continue values from last commit until the present
    #copy the last element and set time to now
    now = int(time.time()) * 1000
    syntax_data.append(copy.copy(syntax_data[-1]))
    syntax_data[-1][0] = now
    line_data.append(copy.copy(line_data[-1]))
    line_data[-1][0] = now

    #interpolate time so syntax bars are full width
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
        
    syntax_data = interpolated_syntax_data

    #substitute
    s = Template(graph_js)
    graphs += s.safe_substitute({'num':file_num,
        'syntax_data':json.dumps(syntax_data),
        'line_data':json.dumps(line_data),
        'bar_width':time_res})

    #for placeholder id
    file_num += 1

#final substitution
with open('graph.html','w') as html:
    s = Template(template)
    html.write(s.safe_substitute(
        {
            'javascript':graphs,
            'placeholders':placeholders,
            'min_time': "%d" % (min_time),
            'max_time': "%d" % now,
            'max_lines': users.get_max_lines() * 1.1,
        }))
