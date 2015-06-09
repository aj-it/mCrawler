import urllib2
import time
import random
from scraping import Scraping
from data.Movie import Movie


opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

err = 0
nid = 123213
while(True):

    sid = str(nid)
    baseUrl = "http://www.imdb.com/title/tt"  + sid.zfill(7)
    print baseUrl
    try:
        request = opener.open(baseUrl)
    except urllib2.HTTPError:
        err +=1
        if(err > 10):
            break

    movie = Scraping.getMovie(request.read())
    print movie

    rand = random.randrange(1,5)
    print "Pause ", rand
    time.sleep(rand)
    nid += 1
print "fin de la boucle"
