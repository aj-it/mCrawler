from Connect import Connect

class Movie:
    @staticmethod
    def save(data):
        connect = Connect()
        cursor = connect.initConnect()
        query = ("INSERT INTO movies "
                       "(title"
                       ", original_title"
                       ", year"
                       ", release_date"
                       ", duration"
                       ", imdb_rating"
                       ", imdb_id"
                       ", imdb_poster)"
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

        data = (data['title']
                      , data['original_title']
                      , data['year']
                      , data['release_date']
                      , data['duration']
                      , data['rating']
                      , data['imdb_id']
                      , data['poster']
                      )
        cursor.execute(query, data)
        connect.commit()

        id_movie = cursor.lastrowid

        connect.closeConnect()

        return id_movie

    @staticmethod
    def addActor(id_movie, id_actor):
        connect = Connect()
        cursor = connect.initConnect()
        query = ("INSERT INTO movies_actors "
                       "(id_movie, id_actor)"
                       "VALUES (%s, %s)")

        data = (id_movie, id_actor)
        cursor.execute(query, data)
        connect.commit()

        connect.closeConnect()

    @staticmethod
    def addGenre(id_movie, id_genre):
        connect = Connect()
        cursor = connect.initConnect()
        query = ("INSERT INTO movies_genres "
                       "(id_movie, id_genre)"
                       "VALUES (%s, %s)")

        data = (id_movie, id_genre)
        cursor.execute(query, data)
        connect.commit()

        connect.closeConnect()

    @staticmethod
    def addDirector(id_movie, id_director):
        connect = Connect()
        cursor = connect.initConnect()
        query = ("INSERT INTO movies_directors "
                       "(id_movie, id_director)"
                       "VALUES (%s, %s)")

        data = (id_movie, id_director)
        cursor.execute(query, data)
        connect.commit()

        connect.closeConnect()

    @staticmethod
    def getMoviesWithoutDirector():
        connect = Connect()
        cursor = connect.initConnect()
        query = ("SELECT id_movie, imdb_id "
                 " FROM movies "
                 " WHERE id_movie NOT IN (SELECT id_movie FROM movies_directors) AND id_movie > 11844")
        cursor.execute(query)
        result = {}
        for (id_movie, imdb_id) in cursor:
            result[id_movie] = imdb_id

        connect.closeConnect()
        return result
        
    