from os.path import isfile, isdir, exists
from shutil import rmtree, copytree, copy2

def copy_dir(src, dest):
    if exists(dest):
        rmtree

    copytree(src,dest)
    
        

def copy(param):
    src = param.src
    dest = param.dest

    if isdir(src):
        copy_dir(src, dest)
    elif isfile(src):
        copy2(src, dest)
    else:
        raise Exception('不支持的复制类型')
        
