from git import *
import compiler
import time

def parse_git(repo_dir,file_path):
    repo = Repo(repo_dir)
    origin = repo.remotes.origin
    #origin.pull()
    repo.iter_commits('master', max_count=100)
    git_data = []
    for iter in repo.iter_commits('master', max_count=100):
        entry = {} 
        entry['hex'] = iter.hexsha
        #times 1000 for javascript flot
        entry['time'] = iter.committed_date * 1000 
#        print(time.asctime(time.gmtime(iter.committed_date)))
        for blob in iter.tree.blobs:
            if iter.tree.blobs[0].path == file_path:
                data = blob.data_stream.read()
                try:
                    compiler.parse(data)
                    entry['syntax'] = True
                except Exception as e:
                    #print("exception!")
                    #print(e)
                    entry['syntax'] = False
                entry['lines'] = len(data.splitlines())
        git_data.append(entry)
    git_data.reverse()
    return git_data

if __name__ == '__main__':
    git_data = parse_git('./work','ttest.py')
    print(git_data)
