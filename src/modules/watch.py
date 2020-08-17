# 用于文件或者目录创建，使用说明参考ansible file模块，部分实现了其中的功能
from os.path import  exists, join, split, splitext
from os import makedirs, stat, walk
from shutil import copy
from functools import reduce
from operator import eq
from .util import getdictvalue
from .handletasks import handletasks
from .cmd_map import cmd_map
from gevent import monkey, spawn
from time import sleep
monkey.patch_all()

oldfilestime = {}


def cmp(dict1, dict2):
    if len(dict1) != len(dict2):
        return 1

    dict1_keys = dict1.keys()
    dict2_keys = dict2.keys()

    if not eq(dict1_keys, dict2_keys):
        return 1

    for key in dict1_keys:
        if dict1[key] != dict2[key]:
            return 1

    return 0


def get_file_names(dirName, exts=[]):
    fileList = []
    for root, _, files in walk(dirName):
        if ".env" in root:
            continue
        if ".git" in root:
            continue
        for file in files:
            fileName = join(root, file)
            if "~" in fileName or "#" in fileName:
                continue
            if splitext(fileName)[1] in exts:
                fileList.append(fileName)

    return fileList


def get_file_time(filePath):
    if not exists(filePath):
        return None

    st = stat(filePath)
    return st.st_mtime or st.st_ctime


def get_target_file_name(source_path, target_path):
    def compose_target_path(file_name):
        return join(target_path, file_name[len(source_path) + 1 :])

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


def getpathobj(pathobj):
    getval = getdictvalue(pathobj)
    return (getval("path"), getval("ext"))


def genentry(filepath):
    obj = {}
    obj[filepath] = get_file_time(filepath)
    return obj


def reduceentries(entries):
    return reduce(lambda x, y: {**x, **y}, entries, {})


def getfilestime(param):
    srcpath = param[0]
    exts = param[1]
    return reduceentries(
        [genentry(filepath) for filepath in get_file_names(srcpath, exts)]
    )


def getcurrentfilestime(paths):
    return reduceentries([getfilestime(getpathobj(path)) for path in paths])


def handle(rootpath, paths, tasks):
    global oldfilestime
    filestime = getcurrentfilestime(
        [{**path, "path": join(rootpath, path["path"])} for path in paths]
    )
    if cmp(filestime, oldfilestime) != 0:
        print('difference found')
        handletasks(cmd_map, rootpath, tasks)
        oldfilestime = filestime


def run(rootpath, interval, paths, tasks):
    if len(tasks) != 0:
        handle(rootpath, paths, tasks)


# 例子
# watch:
#   paths:
#     - path: ./
#       ext:
#         - js


def watch(param):
    getval = getdictvalue(param)
    rootpath = getval("root")
    paths = getval("paths")
    tasks = getval("tasks")
    interval = getval("interval") or 10

    print('begin watch:' + rootpath)
    while True:
        job = spawn(run, rootpath, interval, paths, tasks)
        job.join()
        sleep(interval)
