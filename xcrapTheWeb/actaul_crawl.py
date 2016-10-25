from bs4 import  BeautifulSoup

from  urllib2 import *

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsobj = urlopen(html.read())

for link in bsobj.findAll("a"):
    if 'href' in link.attrs:
        print link.attrs['href']