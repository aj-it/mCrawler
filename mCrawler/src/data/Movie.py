from Connect import Connect

class Movie:
    @staticmethod
    def save(data):
        print "enregistrement d'un film"
        connect = Connect()
        cursor = connect.initConnect()
        query_movie = ("INSERT INTO movies "
                       "(title"
                       ", original_title"
                       ", year"
                       ", release_date"
                       ", duration"
                       ", imdb_rating"
                       ", imdb_id"
                       ", imdb_poster)"
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

        data_movie = (data['title']
                      , data['original_title']
                      , data['year']
                      , data['release_date']
                      , data['duration']
                      , data['rating']
                      , data['imdb_id']
                      , data['poster']
                      )
        print data_movie
        cursor.execute(query_movie, data_movie)
        connect.commit()

        idMovie = cursor.lastrowid

        connect.closeConnect()

        return idMovie


