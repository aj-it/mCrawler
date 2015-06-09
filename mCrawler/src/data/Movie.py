from Connect import Connect

class Movie:
    @staticmethod
    def save(data):
        print "enregistrement d'un film"
        print data
        connect = Connect()
        cursor = connect.initConnect()
        print cursor
        query_movie = ("INSERT INTO movies "
                       "(title, year, duration, rating)"
                       "VALUES (%s, %s, %s, %s)")

        date_movie = (data['title'], data['year'], data['duration'], data['rating'])

        cursor.execute(query_movie, date_movie)
        connect.commit()

        idMovie = cursor.lastrowid

        connect.closeConnect()

        return idMovie


