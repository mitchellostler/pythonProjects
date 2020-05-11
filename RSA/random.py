import datetime

def random(arrLen):
    seed = int(str(datetime.datetime.now().time())[-3:])
    return seed * 8 % arrLen
    
