from fn.func import curried        

@curried
def getdictvalue(param, fieldname):
    return param[fieldname] if fieldname in param else None
