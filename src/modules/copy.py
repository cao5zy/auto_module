from os.path import isfile, isdir

def copy(param):
    src = param.src
    dest = param.dest

    if isdir(src):
        copy_dir(src, dest)
    elif isfile(src):
        copy_file(src, dest)
    else:
        raise Exception('不支持的复制类型')
        
