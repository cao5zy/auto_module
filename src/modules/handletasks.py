from os.path import join, dirname, abspath, exists
from . import copy, file, synchronize
from .util import loadtasks

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

def handletasks(taskpath):
  for config in loadtasks(taskpath):
      if isinstance(config, str):
          handletasks(join(dirname(abspath(taskpath)), config))
      else:
          key = get_cmd_key(config)
          result = cmd_map[key]({**config[key], **{'root': path.dirname(path.abspath(taskpath))}})
          if result == None:
              print("fail at " + key)
              print(config[key])
              break;
    
