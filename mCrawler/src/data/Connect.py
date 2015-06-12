import mysql.connector

class Connect:
    cnx = False
    cursor = False

    def initConnect(self):
        self.cnx = mysql.connector.connect(user='root', password='kinkon', host='91.234.194.132', database='suggmov')
        self.cursor = self.cnx.cursor()
        return self.cursor

    def closeConnect(self):
        self.cursor.close()
        self.cnx.close()

    def commit(self):
        self.cnx.commit()