# 用于文件或者目录创建，使用说明参考ansible file模块，部分实现了其中的功能
from .util import getdictvalue
def file(param):
    getval = getdictvalue(param)
    path = getval('path')
    state = getval('state')
    root = getval('root')
    
