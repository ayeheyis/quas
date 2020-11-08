import psycopg2

# CONSTANTS that shoudld be somethere else
CONNECT_PARAMS = "dbname=quas user=quas password=quas"

class SQLExec:
    def __init__(self):
        pass

    def exec(self, query):
        conn = None
        result = None
        try:
            conn = psycopg2.connect(CONNECT_PARAMS)
            cur = conn.cursor()
            (sql, params) = query.build()
            print(sql)
            cur.execute(sql)
            print("The number of parts: ", cur.rowcount)
            result = cur.fetchall()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return result
    
