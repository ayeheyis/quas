
# Generic Keys
KEY_NAME = "name"


class Field:

    def __init__(self):
        pass

    def init(self, fieldJson):
        if KEY_NAME not in fieldJson:
            return False
        self.name = fieldJson.get(KEY_NAME)
        return True

    def addSelect(self, query):
        query.addField(self.name)
