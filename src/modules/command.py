import subprocess
import sys
from os.path import isdir, exists, join
from os import makedirs
from .util import getdictvalue

def command(param):
    getval = getdictvalue(param)
    chdir = getval('chdir') or ''
    cmd = getval('cmd')
    env = getval('env')
    chenvdir = getval('chenvdir')
    root = getval('root')

    execpath = join(root, chdir) if chdir else root
    envpath = join(root, chenvdir) if chenvdir else root

    def getcmd():
        listcmds = []
        if env:
            listcmds.append('cd {} && {}'.format(envpath, env))

        listcmds.append('cd {} && {}'.format(execpath, cmd))

        return ' && '.join(listcmds)

    cmdstr = getcmd()
    # cmdstr = 'cd /Users/caozy/Documents/projects/auto_module/src/../ && pwd && cd .env/bin/ && source activate'
    print('command:' + cmdstr)
    process = subprocess.Popen(cmdstr, stdout=sys.stdout, stderr=sys.stdout, shell=True, bufsize=0)

    return 0
        
    
