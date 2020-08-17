from fn.func import curried        
from yaml import load
from os.path import exists

@curried
def getdictvalue(param, fieldname):
    return param[fieldname] if fieldname in param else None


def loadtasks(taskpath):
    if not exists(taskpath):
        print('load task fail at:' + taskpath)
        return []
    with open(taskpath, 'r', encoding='utf-8') as yaml_file:
        configs = load(yaml_file)
        return configs['tasks'] or []
