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
while(True):
    nid = Imdb.getLastImdbID()
    sid = str(nid)
        
    movieUrl = "http://www.imdb.com/title/tt"  + sid.zfill(7)
    log = open('main.log', 'a')
    log.write(str(datetime.datetime.now()) + " " + movieUrl + "\n")
    
    try:
        request = opener.open(movieUrl)        
    except urllib2.HTTPError:
        log.write("erreur de connection" + "\n")
        err +=1
        if(err > 10000):
            log.write("Arret du crawl" + "\n")
            break
    except urllib2.URLError:
        log.write("erreur movie url " + movieUrl + "\n")
    else:
        movie = False
        try:
            movie = Scraping.getMovie(request.read())
        except:
            log.write("erreur du crawler " + movieUrl + "\n")

        if (movie != False):
            if(movie['type'] == ''):

                movie['imdb_id'] = nid
                id_movie = False
                try:
                    id_movie = Movie.save(movie)
                except:
                    log.write("can't save movie" + movieUrl + "\n")

                if (id_movie != False):
                    for actor in movie['actors']:
                        id_actor = False
                        try:
                            id_actor = Actor.find(actor.strip())
                        except:
                            log.write("can't find actor" + movieUrl + "\n")
                        if(id_actor == False):
                            try:
                                id_actor = Actor.save(actor.strip())
                            except:
                                log.write("can't save actor" + movieUrl + "\n")
                        if (id_actor == False):
                            try:
                                Movie.addActor(id_movie, id_actor)
                            except:
                                log.write("can't associate actor-movie" + movieUrl + "\n")

                    for genre in movie['genres']:
                        id_genre = False
                        try:
                            id_genre = Genre.find(genre.strip())
                        except:
                            log.write("can't find genre" + movieUrl + "\n")
                        if(id_genre == False):
                            try:
                                id_genre = Genre.save(genre.strip())
                            except:
                                log.write("can't save genre" + movieUrl + "\n")
                            if(id_genre != False):
                                try:
                                    Movie.addGenre(id_movie, id_genre)
                                except:
                                    log.write("can't associate genre-movie" + movieUrl + "\n")

                    time.sleep(1)
                    directorsUrl = "http://www.imdb.com/title/tt{0}/fullcredits?ref_=tt_ov_dr#directors".format(sid)
                    try:
                        request = opener.open(directorsUrl)
                    except urllib2.HTTPError:
                        print "can't to open directory url " + directorsUrl
                    except urllib2.URLError:
                        print "error directory url " + directorsUrl
                    except:
                        log.write("can't open director" + directorsUrl + "\n")
                    else:
                        try:
                            directors = Scraping.getDirectors(request.read())
                        except:
                            log.write("can't scaping" + directorsUrl + "\n")
                        for director in directors:
                            id_director = False
                            try:
                                id_director = Director.find(director.strip())
                            except:
                                log.write("can't find director" + directorsUrl + "\n")
                            if(id_director == False):
                                try:
                                    id_director = Director.save(director.strip())
                                except:
                                    log.write("can't save" + directorsUrl + "\n")

                            if(id_director != False):
                                try:
                                    Movie.addDirector(id_movie, id_director)
                                except:
                                    log.write("can't associate director-movie" + directorsUrl + "\n")

    #rand = random.randrange(1,1)
    time.sleep(1)
    #nid -= 1
    log.close()
