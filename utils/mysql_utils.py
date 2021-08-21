import pymysql


class Database:
    def __init__(self, host, port, user, password, database):

        self.con = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=database,
            cursorclass=pymysql.cursors.DictCursor,
        )
        self.cur = self.con.cursor()

    def query(self, query):
        try:
            self.cur.execute(query)
            result = self.cur.fetchall()
            return result
        except Exception:
            raise

    def insert(self, sql, values):
        result = self.cur.execute(sql, values)
        self.con.commit()
        return result