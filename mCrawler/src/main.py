import urllib2
import time
import random
import datetime
import os

from scraping import Scraping
from data.Movie import Movie
from data.Actor import Actor
from data.Genre import Genre
from data.Director import Director
from data.Imdb import Imdb

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

err = 0
nid = 4766898
while(True):
    last_imdb_id = Imdb.getLastImdbID()
    if(last_imdb_id != False):
        nid = last_imdb_id + 1
        Imdb.save(nid)
    sid = str(nid)
        
    
    movieUrl = "http://www.imdb.com/title/tt"  + sid.zfill(7)
    log = open('main.log', 'a')
    log.write(str(datetime.datetime.now()) + " " + movieUrl + "\n")
    
    try:
        request = opener.open(movieUrl)        
    except urllib2.HTTPError:
        err +=1
        if(err > 10000):
            log.write("Arret du crawl" + "\n")
            break
    else:
        movie = Scraping.getMovie(request.read())                        
        if(movie['type'] == ''):
        
            movie['imdb_id'] = nid        
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

    #rand = random.randrange(1,1)
    time.sleep(1)
    #nid -= 1
    log.close()
