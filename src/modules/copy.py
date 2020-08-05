from os.path import isfile, isdir, exists
from shutil import rmtree, copytree, copy2

        

def copy(param):
    src = param.src
    dest = param.dest

    if isdir(src):
        copytree(src, dest)
    elif isfile(src):
        copy2(src, dest)
    else:
        raise Exception('不支持的复制类型')
        
