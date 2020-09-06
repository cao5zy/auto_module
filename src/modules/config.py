from singleton.singleton import Singleton

@Singleton
class Config(object):
    def __init__(self, vars = []):
        self.vars = vars

def get_vars():
    return Config.instance().vars
