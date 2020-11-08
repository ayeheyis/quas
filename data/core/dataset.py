from .Field import Field
from .Filter import Filter

KEY_NAME = "name"
KEY_TYPE = "type"
KEY_FIELD = "field"
KEY_FILTER = "filter"
KEY_TABLE = "table"

class DataSet:

    def __init__(self):
        self.fields = []
        self.filters = []
        self.table = None

    def init(self, dsJson):
        for obj in dsJson:
            objType = obj.get(KEY_TYPE)
            if objType == KEY_FIELD:
                field = Field()
                field.init(obj)
                self.fields.append(field)
            elif objType == KEY_FILTER:
                filt = Filter()
                filt.init(obj)
                self.filters.append(filt)
            elif objType == KEY_TABLE:
                self.table = obj.get(KEY_NAME)

    def getFields(self):
        return self.fields

    def getFilters(self):
        return self.filters

    def generateQuery(self, query):
        for field in self.fields:
            field.addSelect(query)

        for f in self.filters:
            f.addWhere(query)

        query.addTable(self.table)