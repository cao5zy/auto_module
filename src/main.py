import sys
from yaml import load, dump
from modules import handletasks, cmd_map, watch
from os import path
from os.path import join, dirname, abspath, exists
from optparse import OptionParser 
# import codecs
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) 

parser = OptionParser()

def get_config_path ():
    args = parser.parse_args()
    print('args:')
    print(args[1][0])
    return args[1][0] 

def main():
    handletasks({**cmd_map, "watch": watch}, get_config_path())
    

if __name__ == '__main__':
    main()
