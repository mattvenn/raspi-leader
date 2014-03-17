#from git import *
from config import *
import compiler
import time
import pprint
import subprocess
import os

pp = pprint.PrettyPrinter()

#manage a bunch of users
class Users:
    def __init__(self):
        self.users = []

    def get_user(self,host,name):
        for user in self.users:
            if user.host == host and user.name == name:
                return user
        return None

    def add_user(self,host,name,filename):
        new_user = User(host,name,filename)
        self.users.append(new_user)
        return new_user

    def get_users(self):
        return self.users
   
#each user
class User:
    def __init__(self,host,name,filename):
        self.host = host
        self.name = name
        self.filename = filename
        self.history = []

    def get_path(self):
        return os.path.join(local_dir,self.host,self.name,self.filename)

    def get_link(self):
        return "%s@%s:%s" % (self.name, self.host, self.filename)

    #don't track old files
    def add_version(self,filename,version):
        #if it's a different file, chuck out the old history
        if filename != self.filename:
            self.history = []
        self.history.append(version)

    def get_history(self):
        return self.history[::-1]

    def pprint(self):
        print(self.host,self.name,self.filename)
        for history in self.history:
            history.pprint()

#represents each version of a file
class History:
    def __init__(self,hex,time,lines,syntax):
        self.hex = hex
        self.time = time
        self.lines = lines
        self.syntax = syntax

    def pprint(self):
        print(self.hex,self.time,self.lines,self.syntax)

#populates the Users object with details of each user's files.
#each version of a file is represented by a history object
def fetch_git(repo_dir):

    #create new user object
    users = Users()
    os.chdir(repo_dir)
    os.system('git checkout master -q')
    proc = subprocess.Popen(['git', 'log', '--pretty=format:%H %ct'],stdout=subprocess.PIPE)
    commit_log = proc.stdout.readlines()
    for log in commit_log:
        log = log.strip()
        (commit,date) = log.split(' ')
        os.system('git checkout ' + commit + ' -q')
    #    print(commit,date)
        proc = subprocess.Popen(['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', commit],stdout=subprocess.PIPE)
        changes = proc.stdout.readlines()
        #print(changes)
        for change in changes:
            path = change.strip()
            dir,filename = os.path.split(path)
            host,name = os.path.split(dir)
    
            user = users.get_user(host,name)
            if user == None:
                user = users.add_user(host,name,filename)

            try:
                with open(path) as fh:
                    data = fh.read()
                    try:
                        compiler.parse(data)
                        syntax = True
                    except Exception as e:
                        #print("exception!")
                        #print(e)
                        syntax = False
                    lines = len(data.splitlines())
            except IOError:
                continue

            #times 1000 for javascript flot
            time = int(date) * 1000 
            history = History(commit,time,lines,syntax)
            user.add_version(filename,history)

    os.chdir('..')
    return users

if __name__ == '__main__':
    users = fetch_git(local_dir)
    for user in users.get_users():
        user.pprint()
