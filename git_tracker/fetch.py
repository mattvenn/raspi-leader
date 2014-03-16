"""
* fetch all directories under pi:~/work/
* copy to local repo
* add and commit
"""

import os
import shutil
import pygit
user_name = 'pi'
work_dir = '~/work'
from config import *

def init():
    #remove work directory
    try:
        shutil.rmtree(local_dir)
    except OSError:
        #dir doesn't exist
        pass

    #set up new work directory and host subdirs
    os.mkdir(local_dir)
    for host in host_ips:
        os.mkdir(local_dir+'/'+host)

    #set git up
    git_setup = 'git init %s' % local_dir
    os.system(git_setup)

def update():
    #for each host
    for host_ip in host_ips:
        scp_command = 'scp -r %s@%s:%s/* %s/%s/' % (user_name,host_ip,work_dir,local_dir,host_ip)
        print(scp_command)
        os.system(scp_command)

    os.chdir(local_dir)
    #add all python files
    os.system('git add -A *py')
    os.system('git commit --allow-empty-message  -m ""')
    os.chdir('..')

#return most recently changed file from each directory on each host
def get_recent_files():
    dirs = []
    for host_ip in host_ips:
        for dir in os.listdir(local_dir + '/' + host_ip):
            dirs.append(dir)
    return dirs


if __name__ == '__main__':
    #init()
    update()
    dirs = get_recent_files()
    git_data = pygit.parse_git(local_dir)
    for host_ip in host_ips:
        for dir in dirs:
            git_data = pygit.parse_git(local_dir + '/' + host_ip + '/' + dir)
            print git_data
