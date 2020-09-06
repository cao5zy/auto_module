from os.path import isfile, isdir, exists, join
from shutil import rmtree, copytree, copy2
from .util import getdictvalue
from jinja2 import Environment, FileSystemLoader
from .config import get_vars
# jinja2 模板 https://palletsprojects.com/p/jinja/
# 具体参考 http://docs.jinkan.org/docs/jinja2/templates.html

def writeContent(destpath, content):
    try:
        with open(destpath, 'w') as fileObj:
            fileObj.write(content)
    except Exception as ex:
        raise ValueError('%s\n writeContent:%s' % (repr(ex), destpath))
    
def template(param):
    getval = getdictvalue(param)
    src = getval('src')
    dest = getval('dest')
    root = getval('root')

    srcpath = join(root, src)
    destpath = join(root, dest)

    if not exists(srcpath):
        raise FileNotFoundError(srcpath)

    try:
        env = Environment(loader=FileSystemLoader(root))
        tpl = env.get_template(src)
        writeContent(destpath, tpl.render(get_vars()))
    except Exception as ex:
        raise ValueError('%s\n template:%s'%(repr(ex), srcpath))

    return 0
        
