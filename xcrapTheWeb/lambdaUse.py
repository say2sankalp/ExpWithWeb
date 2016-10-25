from bs4 import  BeautifulSoup
from urllib2 import *

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj = BeautifulSoup(html.read())

tags = bsobj.findAll(lambda tag : len(tag.attrs)==2)

for item in tags:
    print item