from os.path import join, dirname, abspath, isfile
from .util import loadtasks



def get_cmd_key(config, cmd_keys):
    config_keys = [key for key in config]
    keys = list(set(cmd_keys).intersection(set(config_keys)))
    if len(keys) == 0:
        raise Exception("该命令没有包含在:" + ",".join(config_keys))

    return keys[0]


def get_taskpath(taskpath):
    if isfile(taskpath):
        return dirname(abspath(taskpath))
    else:
        return taskpath
                    
def handletasks(cmd_map, taskpath, tasks=[]):
    for config in tasks if len(tasks) > 0 else loadtasks(taskpath):
        if isinstance(config, str):
            handletasks(cmd_map, join(get_taskpath(taskpath), config))
        else:
            try:
                if config['name']:
                    print('> ' + config['name'])
                cmd_keys = [key for key in cmd_map]
                key = get_cmd_key(config, cmd_keys)
                result = cmd_map[key](
                    {**config[key], **{"root": get_taskpath(taskpath)}}
                )
                if result is None:
                    print("fail at " + key)
                    print(config[key])
                    break
            except Exception as ex:
                print('handle tasks error')
                print(config)
                raise ex
