import pymysql

class MyDataBase:
    def __init__(self,database='spider'):
#         print("connect to data base......")
        self.db = pymysql.connect("localhost","root","root",database,charset='utf8')
        self.cursor = self.db.cursor()
        self.db.autocommit(True)
#         print("connect success!")

    def getConn(self):
        return self.db

    def getExcuter(self):
        return self.cursor

    def close(self):
        self.cursor.close()
        self.db.close()