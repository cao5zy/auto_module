import sys
from yaml import load, dump
from modules import copy
from os.path import abspath, dirname
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

def get_config_root_path():
    return dirname(abspath(get_config_path()))


def main():
    print(get_config_path())
    print(get_config_root_path())
    print(cmd_keys)
    with open(get_config_path(), 'r', encoding='utf-8') as yaml_file:
        configs = load(yaml_file)
        for config in configs:
            cmd_key = get_cmd_key(config)
            cmd = cmd_map[cmd_key]
            config1 =config[cmd_key].copy()
            config1['dir'] = get_config_root_path()
            cmd(config1)

if __name__ == '__main__':
    main()
