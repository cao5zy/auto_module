from os.path import isdir, exists, join
from os import makedirs
from .util import getdictvalue
import subprocess

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
    
    process = subprocess.Popen(cmdstr, stdout=subprocess.PIPE, shell=True, bufsize=1)
    for line in iter(process.stdout.readline, b''):
        print(str(line, encoding='utf-8').replace('\n', ''))

    return 0
        
    
