import sys
from yaml import load, dump
from modules import handletasks, cmd_map, watch
from os import path
from os.path import join, dirname, abspath, exists
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) 

def get_config_path ():
    return sys.argv[1] 

def main():
    handletasks({**cmd_map, "watch": watch}, get_config_path())
    

if __name__ == '__main__':
    main()
