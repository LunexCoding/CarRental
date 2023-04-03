import pymysql
from settingsConfig import settingsConfig


class DatabaseConnection(object):
    def __init__(self, __settings):
        self.__settings = __settings
        self.__settings["cursorclass"] = pymysql.cursors.DictCursor
        self.dbConn = None
        self.dbCursor = None

    def __enter__(self):
        self.dbConn = pymysql.connect(**self.__settings, autocommit=True)
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


databaseSession = DatabaseConnection(settingsConfig.DatabaseSettings)
