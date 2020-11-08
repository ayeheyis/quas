QUERY = "SELECT %s FROM %s"
WHERE = "WHERE %s"
KEY_SELECT = "select"
KEY_TABLE = "table"
KEY_WHERE = "where"
CLAUSES = [KEY_SELECT, KEY_TABLE, KEY_WHERE]

class SQLQuery:
    def __init__(self):
        self.query = {}
        self.params = []
        self.query[KEY_SELECT] = []
        self.query[KEY_TABLE] = "empty"
        self.query[KEY_WHERE] = []
    
    def addField(self, field):
        self.query[KEY_SELECT].append(field)

    def addTable(self, table):
        self.query[KEY_TABLE] = table

    def addWhere(self, condition, param=None):
        if param is not None:
            self.params.append(param)
        self.query[KEY_WHERE].append(condition)

    def build(self):
        selClause = ', '.join(self.query[KEY_SELECT])
        table = self.query[KEY_TABLE]
        sql = QUERY % (selClause, table)
        if self.query[KEY_WHERE]:
            whereClause = 'AND '.join(self.query[KEY_WHERE])
            sql += " " + (WHERE % whereClause)
        return (sql, self.params)