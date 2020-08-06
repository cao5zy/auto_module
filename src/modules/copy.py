from os.path import isfile, isdir, exists
from shutil import rmtree, copytree, copy2

        

def copy(param):
    print(param)
    src = param['src']
    dest = param['dest']

    if isdir(src):
        return copytree(src, dest)
    elif isfile(src):
        return copy2(src, dest)
    else:
        raise Exception('不支持的复制类型')
        
