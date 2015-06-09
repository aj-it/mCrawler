import urllib2
import time
import random
from scraping import Scraping
from data.Movie import Movie


opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

err = 0
nid = 1371111
while(True):

    sid = str(nid)
    movieUrl = "http://www.imdb.com/title/tt"  + sid.zfill(7)
    print movieUrl
    try:
        request = opener.open(movieUrl)
    except urllib2.HTTPError:
        err +=1
        if(err > 10):
            break
    else:
        movie = Scraping.getMovie(request.read())

        directorsUrl = "http://www.imdb.com/title/tt{0}/fullcredits?ref_=tt_ov_dr#directors".format(sid)
        try:
            request = opener.open(directorsUrl)
        except urllib2.HTTPError:
            pass
        else:
            directors = Scraping.getDirectors(request.read())

        movie['directors'] = directors
    movie['imdb_id'] = sid
    print movie

    Movie.save(movie)

    rand = random.randrange(1,5)
    time.sleep(rand)
    nid += 1
print "fin de la boucle"
