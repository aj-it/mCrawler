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
                result = 0
            else:
                result = int(last_imdb_id[0])
            break

        connect.closeConnect()
        return result
    
    @staticmethod
    def save(id_imdb):
        connect = Connect()
        cursor = connect.initConnect()
        query = ("INSERT INTO imdb "
                       "(id_imdb)"
                       "VALUES (%s)")

        data = (id_imdb,)
        cursor.execute(query, data)
        connect.commit()
        connect.closeConnect()