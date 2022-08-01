"""This python program executes your code
"""

from git import Repo
import os
import time
import sys
import subprocess


#advanced feature change at your own risk
COMPILER_COMMAND = 'python' # replace with whatever usually used in the commandline ex. python3



def check_diff(repo):
    hcommit = repo.head.commit
    
    diffs = hcommit.diff(None)

    if len(diffs) == 0:
        return False
    else:
        return True


def add_commit(id, check_changed = True, push = True):
    """
    Add current changes and commit
    """
    # need to check if anything in repo has changed
    repo = Repo(os.path.dirname(os.getcwd())) #changed to look at the parent
    
    if check_changed:
        changed = check_diff(repo)
    else:
        changed = True    
        
    if changed:
        repo.git.add('.')
        
        repo.git.commit('-m', id)
        if push:
            repo.remotes.origin.push()
        return changed
    
    else:
        return changed

      
if __name__ == '__main__':
    
    ##error checking
    if len(sys.argv) == 1:
        print("You must run the program as follows:\n python run.py scratch.py \n or \n python run.py load.py \n or \n python run.py plot.py")
        exit()
    
              
    id = str(time.time())
    committed = add_commit(id + '_start', push = False)
    
    command = [COMPILER_COMMAND] + sys.argv[1:]

    process = subprocess.run(command)
    
    with open('./runs.txt', 'a') as f:
        record = '{} , {}, {} , error_code: {} \n'.format(sys.argv[1], committed, id, process.returncode)
        f.write(record)

    add_commit(id + '_end', check_changed = False, push=True)
