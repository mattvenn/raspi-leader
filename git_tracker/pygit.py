#from git import *
from config import *
import compiler
import time
import pprint
import subprocess
import os

def fetch_git(repo_dir):
    os.chdir(repo_dir)
    git_data = []
    os.system('git checkout master')
    proc = subprocess.Popen(['git', 'log', '--pretty=format:%H %ct'],stdout=subprocess.PIPE)
    commit_log = proc.stdout.readlines()
    for log in commit_log:
        log = log.strip()
        (commit,date) = log.split(' ')
        os.system('git checkout ' + commit)
    #    print(commit,date)
        proc = subprocess.Popen(['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', commit],stdout=subprocess.PIPE)
        changes = proc.stdout.readlines()
        #print(changes)
        for change in changes:
            file_name = change.strip()
            entry = {} 
            entry['name'] = file_name
            try:
                with open(file_name) as fh:
                    data = fh.read()
                    try:
                        compiler.parse(data)
                        entry['syntax'] = True
                    except Exception as e:
                        #print("exception!")
                        #print(e)
                        entry['syntax'] = False
                    entry['lines'] = len(data.splitlines())
            except IOError:
                continue

            entry['hex'] = commit
            #times 1000 for javascript flot
            entry['time'] = int(date) * 1000 
            git_data.append(entry)
    git_data.reverse()
    os.chdir('..')
    return git_data

if __name__ == '__main__':
    git_data = fetch_git(local_dir)
    pp = pprint.PrettyPrinter()
    pp.pprint(git_data)
