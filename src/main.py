import sys
from yaml import load, dump
from modules import handletasks
from os import path
from os.path import join, dirname, abspath, exists

    
def get_config_path ():
    return sys.argv[1] 

def handle(taskpath):
    print('handletasks')
    print(taskpath)
    if not exists(taskpath):
        print('follow task not exists')
        print(taskpath)
        return
    
    handletasks(taskpath)
    

def main():
    print(get_config_path())
    handle(get_config_path())
        
    

if __name__ == '__main__':
    main()
