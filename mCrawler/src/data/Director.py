from Connect import Connect

class Director:

    @staticmethod
    def find(name):
        connect = Connect()
        cursor = connect.initConnect()

        query = ("SELECT id_director, name "
                 "FROM directors "
                 "WHERE name = %s "
                 "ORDER BY id_director ASC")
        data = (name,)
        cursor.execute(query, data)
        result = False
        for (id_director, name) in cursor:
            result = id_director
            break

        connect.closeConnect()
        return result

    @staticmethod
    def save(name):
        connect = Connect()
        cursor = connect.initConnect()
        query = ("INSERT INTO directors "
                       "(name)"
                       "VALUES (%s)")

        data = (name,)
        cursor.execute(query, data)
        connect.commit()

        id_director = cursor.lastrowid

        connect.closeConnect()

        return id_director
