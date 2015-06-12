import lxml.html
from HTMLParser import HTMLParser

class Scraping:
    @staticmethod
    def getMovie(html):
        hxs = lxml.html.document_fromstring(html)
        hp = HTMLParser()
        movie = {}
        try:
            movie['title'] = hp.unescape(hxs.xpath('//*[@id="overview-top"]/h1/span[1]/text()')[0].strip())
        except IndexError:
            movie['title'] = ""
        try:
            original_title = hxs.xpath('//*[@id="overview-top"]/h1/span[3]/text()')[0].strip()
            movie['original_title'] = original_title.replace('"', '')
        except IndexError:
            movie['original_title'] = ""
            
        try:
            movie['type'] = hxs.xpath('//*[@id="overview-top"]/div[1]/text()')[0].strip()        
        except IndexError:
            movie['type'] = ""
        try:
            movie['year'] = hxs.xpath('//*[@id="overview-top"]/h1/span[2]/a/text()')[0].strip()
        except IndexError:
            try:
                movie['year'] = hxs.xpath('//*[@id="overview-top"]/h1/span[3]/a/text()')[0].strip()
            except IndexError:
                movie['year'] = ""
        try:
            duration = hxs.xpath('//*[@id="overview-top"]/div[2]/time/text()')[0].strip()
            movie['duration'] = int(duration.replace('min', '').strip())
        except IndexError:
            movie['duration'] = 0
        try:
            movie['genres'] = hxs.xpath('//*[@id="overview-top"]/div[2]/a/span/text()')
        except IndexError:
            movie['genres'] = []
        try:
            movie['release_date'] = hxs.xpath('//*[@id="overview-top"]/div[2]/span[3]/a/text()')[0].strip()
        except IndexError:
            try:
                movie['release_date'] = hxs.xpath('//*[@id="overview-top"]/div[2]/span[4]/a/text()')[0].strip()
            except Exception:
                movie['release_date'] = ""
        try:
            movie['rating'] = float(hxs.xpath('//*[@id="overview-top"]/div[3]/div[3]/strong/span/text()')[0].strip())
        except IndexError:
            movie['rating'] = 0

        try:
            movie['poster'] = hxs.xpath('//*[@id="img_primary"]/div/a/img/@src')[0].strip()
        except IndexError:
            movie['poster'] = ""

        try:
            movie['actors'] = hxs.xpath('//*[@id="overview-top"]/div[6]/a/span/text()')
        except IndexError:
            movie['actors'] = ""

        return movie

    @staticmethod
    def getDirectors(html):
        hxs = lxml.html.document_fromstring(html)
        directors = []
        try:
            data = hxs.xpath('//*[@id="fullcredits_content"]/table[1]/tbody/tr/td/a/text()')
            for d in data:
                directors.append(d.strip())
        except IndexError:
            pass

        return directors