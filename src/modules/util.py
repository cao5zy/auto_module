from fn.func import curried        
from yaml import load

@curried
def getdictvalue(param, fieldname):
    return param[fieldname] if fieldname in param else None


def loadtasks(taskpath):
    with open(taskpath, 'r', encoding='utf-8') as yaml_file:
        configs = load(yaml_file)
        return configs['tasks']
