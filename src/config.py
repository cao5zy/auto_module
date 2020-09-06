from singleton.singleton import Singleton

@Singleton
class Config(object):
    def __init__(self, vars = []):
        self.vars = vars

def getVars():
    return Config.instance().vars
