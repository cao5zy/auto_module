# 用于文件或者目录创建，使用说明参考ansible file模块，部分实现了其中的功能
from os.path import isdir, exists, join, split
from os import makedirs, stat, walk
from .util import getdictvalue
from shutil import copy

def get_file_names(dirName):
    fileList = []
    for root, dirs, files in walk(dirName):
        if('.env' in root):continue
        if('.git' in root):continue
        for file in files:
            fileName = join(root,file)
            if '~' in fileName or '#' in fileName :continue
            fileList.append(fileName)
    return fileList

def get_file_time(filePath):
    if not exists(filePath): return None
    
    st = stat(filePath)
    return st.st_mtime or st.st_ctime

def get_target_file_name(source_path, target_path):
    def compose_target_path(file_name):
        # print('get_target_file_name')
        # print(source_path)
        # print(target_path)
        # print(file_name)
        result =  join(target_path, file_name[len(source_path):])
        print('copied:' + result)
        return result
    return compose_target_path

def get_copy_file(get_target_path):
    def copy_file(source_file):
        copy(source_file, get_target_path(source_file))
    return copy_file

def ensure_target_dir(get_target_path):
    def create_target_dir(source_file):
        target_dir = split(get_target_path(source_file))[0]
        if not exists(target_dir):
            makedirs(target_dir)
    return create_target_dir


def sync(srcpath, destpath):
    get_destpath = get_target_file_name(srcpath, destpath)
    copy_file = get_copy_file(get_destpath)
    ensure_dir = ensure_target_dir(get_destpath)

    def filter_files(source, target):
        return get_file_time(target) == None or get_file_time(source) > get_file_time(target)

    transferred_files = filter(lambda f:filter_files(f, get_destpath(f)), get_file_names(srcpath))

    for source_file in transferred_files:
        ensure_dir(source_file)
        copy_file(source_file)


    return 0
    
def synchronize(param):
    getval = getdictvalue(param)
    root = getval('root')
    src = getval('src')
    dest = getval('dest')

    srcpath = join(root, src)
    destpath = join(root, dest)

    if not exists(srcpath):
        raise Exception('src is not valid: ' + srcpath)

    if not exists(destpath):
        raise Exception('dest is not valid: ' + destpath)

    return sync(srcpath, destpath)
        
    
