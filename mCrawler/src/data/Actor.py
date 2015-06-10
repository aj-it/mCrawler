from Connect import Connect

class Actor:

    @staticmethod
    def find(name):
        connect = Connect()
        cursor = connect.initConnect()

        query = ("SELECT id_actor, name "
                 "FROM actors "
                 "WHERE name = %s "
                 "ORDER BY id_actor ASC")
        data = (name,)
        cursor.execute(query, data)
        result = False
        for (id_actor, name) in cursor:
            result = id_actor
            break

        connect.closeConnect()
        return result

    @staticmethod
    def save(name):
        connect = Connect()
        cursor = connect.initConnect()
        query = ("INSERT INTO actors "
                       "(name)"
                       "VALUES (%s)")

        data = (name,)
        cursor.execute(query, data)
        connect.commit()

        id_actor = cursor.lastrowid

        connect.closeConnect()

        return id_actor
