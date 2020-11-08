# Generic Keys
KEY_PARAM = "param"

class Filter:
    def __init__(self):
        pass

    def init(self, filterJson):
        if KEY_PARAM not in filterJson:
            return False
        param = filterJson.get(KEY_PARAM)
        self.name = param[0]
        self.value = param[1]
        self.operation = param[2]
        return True

    def addWhere(self, query): 
        clause = "(%s %s '%s')" % (self.name, self.operation, self.value)
        query.addWhere(clause)