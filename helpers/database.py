import pymysql
from decouple import config


db_config = {
    'host': config("DB_HOST", default=""),
    'port': int(config("DB_PORT", default="")),
    'user': config("DB_USER", default=""),
    'password': config("DB_PASSWORD", default=""),
    'database': "AutoService",
    'cursorclass': pymysql.cursors.DictCursor
}


class DatabaseConnection(object):
    def __init__(self, db_local):
        self.db_local = db_local
        self.dbConn = None
        self.dbCursor = None

    def __enter__(self):
        self.dbConn = pymysql.connect(**self.db_local, autocommit=True)
        self.dbCursor = self.dbConn.cursor()
        return self

    def __exit__(self, exception_type, exception_val, trace):
        try:
            self.dbCursor.close()
            self.dbConn.close()
        except AttributeError:
            return True

    def execute(self, sql, data=None):
        if data is not None:
            self.dbCursor.execute(sql, data)
        else:
            self.dbCursor.execute(sql)
        self.dbConn.commit()

    def getRows(self, sql, data=None):
        self.dbCursor.execute(sql)
        return self.dbCursor.fetchall()


databaseSession = DatabaseConnection(db_config)
