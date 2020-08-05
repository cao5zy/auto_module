import sys
from yaml import load, dump
from modules import copy

def get_config_path ():
    return sys.argv[1]


def main():
    print(get_config_path())
    cmd_map = {
        "copy": copy
    }
    cmd_keys = [key for key in cmd_map]
    print(cmd_keys)
    with open(get_config_path(), 'r', encoding='utf-8') as yaml_file:
        configs = load(yaml_file)
        for config in configs:
            config_keys = [key for key in config]
            keys = list(set(cmd_keys).intersection(set(config_keys)))
            print(keys)
            print(config[keys[0]])
        
    

if __name__ == '__main__':
    main()
