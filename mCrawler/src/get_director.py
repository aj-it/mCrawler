import urllib2
import time
import random
import datetime
import os

from scraping import Scraping
from data.Movie import Movie
from data.Director import Director

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

movies = Movie.getMoviesWithoutDirector()
for id_movie in movies:
    print movies[id_movie]
    sid = str(movies[id_movie])
    sid.zfill(7)
    directorsUrl = "http://www.imdb.com/title/tt{0}/fullcredits?ref_=tt_ov_dr#directors".format(sid)

    try:
        request = opener.open(directorsUrl)
    except urllib2.HTTPError:
        print "can't to open directory url " + directorsUrl
    except urllib2.URLError:
        print "error directory url " + directorsUrl
    else:
        directors = Scraping.getDirectors(request.read())
        for director in directors:
            id_director = Director.find(director.strip())
            if(id_director == False):
                id_director = Director.save(director.strip())

            if(id_director != False):
                Movie.addDirector(id_movie, id_director)
                print "asso " + id_movie + " " + id_director
    time.sleep(1)
