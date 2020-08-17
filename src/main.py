import sys
from yaml import load, dump
from modules import copy, file, synchronize
from os import path
from os.path import join, dirname, abspath, exists

cmd_map = {
    "copy": copy,
    "file": file,
    "synchroize": synchronize
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

def handletasks(taskpath):
    print('handletasks')
    print(taskpath)
    if not exists(taskpath):
        print('follow task not exists')
        print(taskpath)
        return
    
    with open(taskpath, 'r', encoding='utf-8') as yaml_file:
        configs = load(yaml_file)
        for config in configs['tasks']:
            if isinstance(config, str):
                handletasks(join(dirname(abspath(taskpath)), config))
            else:
                key = get_cmd_key(config)
                result = cmd_map[key]({**config[key], **{'root': path.dirname(path.abspath(taskpath))}})
                if result == None:
                    print("fail at " + key)
                    print(config[key])
                    break;
    

def main():
    print(get_config_path())
    print(cmd_keys)
    handletasks(get_config_path())
        
    

if __name__ == '__main__':
    main()
