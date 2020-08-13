from os.path import isfile, isdir, exists, join
from shutil import rmtree, copytree, copy2

        

def copy(param):
    src = param['src'] if 'src' in param else None
    dest = param['dest'] if 'dest' in param else None
    root = param['root'] if 'root' in param else None

    srcpath = join(root, src)
    destpath = join(root, dest)
    
    if isdir(srcpath):
        copytree(srcpath, destpath)
    elif isfile(srcpath):
        copy2(srcpath, destpath)
    else:
        raise Exception('not supported file type')
        
