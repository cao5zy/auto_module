from os.path import isfile, isdir, exists, join
from shutil import rmtree, copytree, copy2
from .util import getdictvalue

def copy(param):
    getval = getdictvalue(param)
    src = getval('src')
    dest = getval('dest')
    root = getval('root')

    srcpath = join(root, src)
    destpath = join(root, dest)
    
    if isdir(srcpath):
        copytree(srcpath, destpath)
    elif isfile(srcpath):
        copy2(srcpath, destpath)
    else:
        raise Exception('not supported file type')
        
