# 用于文件或者目录创建，使用说明参考ansible file模块，部分实现了其中的功能
from os.path import isdir, exists, join
from os import makedirs, symlink
from .util import getdictvalue


def createdir(realpath):
    if exists(realpath):
        return 0
    else:
        try:
            makedirs(realpath)
            return 0
        except Exception as e:
            return None

def createlink(source, dest):
    if exists(dest):
        return 0
    symlink(source, dest)
    return 0
    
def file(param):
    getval = getdictvalue(param)
    path = getval('path')
    state = getval('state')
    src = getval('src')
    root = getval('root')

    realpath = join(root, path)

    if state == 'directory':
        return createdir(realpath)
    elif state == 'link':
        source = join(root, src)
        return createlink(source, realpath)
    else:
        raise Exception('not supported state, state should be: directory')
        
    
