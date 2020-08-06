import sys
from yaml import load, dump
from modules import copy

cmd_map = {
    "copy": copy
}

cmd_keys = [key for key in cmd_map]

def get_cmd_key(config):
    config_keys = [key for key in config]
    keys = list(set(cmd_keys).intersection(set(config_keys)))
    if len(keys) == 0:
        raise Exception('该命令没有包含在:' + ','.join(config_keys))
    
    return keys[0]
    
def get_config_path ():
    return sys.argv[1]

def main():
    print(get_config_path())
    print(cmd_keys)
    with open(get_config_path(), 'r', encoding='utf-8') as yaml_file:
        configs = load(yaml_file)
        for config in configs:
            cmd = cmd_map[get_cmd_key(config)]
            cmd(config)

if __name__ == '__main__':
    main()
