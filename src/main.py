import sys
from yaml import load, dump
from modules import handletasks, cmd_map, watch, Config, get_vars
from os import path
from os.path import join, dirname, abspath, exists
from optparse import OptionParser
from functools import reduce
# import codecs
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) 

parser = OptionParser()
parser.add_option('-e', '--extra-vars', action='append', type='string', dest='vars', default=[])
def get_config_path ():
    (_, args) = parser.parse_args()
    return args[0] 

def parse(var):
    try:
        items = var.split('=')
        obj = {}
        obj[items[0]] = items[1]
        return obj
    except Exception as ex:
        raise ValueError(repr(ex) + '\n' + 'parse error: ' + (var or '') )

def main():
    (options, args) = parser.parse_args()
    Config.initialize(vars=reduce(lambda x,y:{**x,**y}, [parse(var) for var in options.vars], {}))
    print('args:')
    print(args)
    print('options')
    print(get_vars())

    handletasks({**cmd_map, "watch": watch}, get_config_path())
    

if __name__ == '__main__':
    main()
