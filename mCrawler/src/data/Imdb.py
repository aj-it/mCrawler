from Connect import Connect

class Imdb:
    
    @staticmethod
    def getLastImdbID():
        connect = Connect()
        cursor = connect.initConnect()

        query = ("SELECT MAX(id_imdb) AS last_imdb_id "
                 "FROM imdb ")
        cursor.execute(query)
        result = False
        for (last_imdb_id) in cursor:
            if(last_imdb_id[0] == None):
                last_imdb_id = 0
            else:
                last_imdb_id = int(last_imdb_id[0])
            break

        nid = last_imdb_id + 1
        try:
            Imdb.save(nid)
        except mysql.connector.Error:
            nid = self.getLastImdbID()
        connect.closeConnect()
        return nid
    
    @staticmethod
    def save(id_imdb):
        connect = Connect()
        cursor = connect.initConnect()
        query = ("INSERT INTO imdb "
                       "(id_imdb)"
                       "VALUES (%s)")

        data = (id_imdb,)
        try:
            cursor.execute(query, data)
        except mysql.connector.Error:
            raise
        connect.commit()
        connect.closeConnect()