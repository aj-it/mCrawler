import mysql.connector
import os
class Connect:
    cnx = False
    cursor = False

    def initConnect(self):
        user=''
        password=''
        host=''
        database=''
        path = '/home/mCrawler'
        config = open(path + '/mCrawler/src/data/config.ini', 'r')
        for conf in config:
            
            data= conf.split(':')
            if (data[0] == 'user'):
                u = data[1].strip()
            if (data[0] == 'password'):
                p = data[1].strip()
            if (data[0] == 'host'):
                h = data[1].strip()
            if (data[0] == 'database'):
                d = data[1].strip()
                
        self.cnx = mysql.connector.connect(user=u, password=p, host=h, database=d)
        self.cursor = self.cnx.cursor()
        return self.cursor

    def closeConnect(self):
        self.cursor.close()
        self.cnx.close()

    def commit(self):
        self.cnx.commit()