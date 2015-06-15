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
for movie in movies:
    print movie
    exit(0)
