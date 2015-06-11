import urllib2
import time
import random
import datetime

from scraping import Scraping
from data.Movie import Movie
from data.Actor import Actor
from data.Genre import Genre
from data.Director import Director

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

err = 0
#nid = 1371111
nid = 4766898
while(True):

    sid = str(nid)
    movieUrl = "http://www.imdb.com/title/tt"  + sid.zfill(7)
    print str(datetime.datetime.now()) + " " + movieUrl
    try:
        request = opener.open(movieUrl)        
    except urllib2.HTTPError:
        err +=1
        if(err > 1000):
            break
    else:
        movie = Scraping.getMovie(request.read())        
        print movie
        if(movie['type'] == ''):
        
            movie['imdb_id'] = sid.zfill(7)        
            id_movie = Movie.save(movie)

            for actor in movie['actors']:
                id_actor = Actor.find(actor.strip())
                if(id_actor == False):
                    id_actor = Actor.save(actor.strip())
                Movie.addActor(id_movie, id_actor)

            for genre in movie['genres']:
                id_genre = Genre.find(genre.strip())
                if(id_genre == False):
                    id_genre = Genre.save(genre.strip())
                Movie.addGenre(id_movie, id_genre)

            directorsUrl = "http://www.imdb.com/title/tt{0}/fullcredits?ref_=tt_ov_dr#directors".format(sid)
            try:
                request = opener.open(directorsUrl)
            except urllib2.HTTPError:
                pass
            else:
                directors = Scraping.getDirectors(request.read())
                for director in directors:
                    id_director = Director.find(director.strip())
                    if(id_director == False):
                        id_director = Director.save(director.strip())
                    Movie.addDirector(id_movie, id_director)

    rand = random.randrange(1,1)
    time.sleep(rand)
    nid -= 1
