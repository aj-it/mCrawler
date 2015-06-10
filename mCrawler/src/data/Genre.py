from Connect import Connect

class Genre:

    @staticmethod
    def find(name):
        connect = Connect()
        cursor = connect.initConnect()

        query = ("SELECT id_genre, name "
                 "FROM genres "
                 "WHERE name = %s "
                 "ORDER BY id_genre ASC")
        data = (name,)
        cursor.execute(query, data)
        result = False
        for (id_genre, name) in cursor:
            result = id_genre
            break

        connect.closeConnect()
        return result

    @staticmethod
    def save(name):
        connect = Connect()
        cursor = connect.initConnect()
        query = ("INSERT INTO genres "
                       "(name)"
                       "VALUES (%s)")

        data = (name,)
        cursor.execute(query, data)
        connect.commit()

        id_genre = cursor.lastrowid

        connect.closeConnect()

        return id_genre
