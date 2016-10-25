from bs4 import  BeautifulSoup
from urllib2 import *

html = urlopen("http://www.pythonscraping.com/pages/page3.html")

bsobj = BeautifulSoup(html.read())

print bsobj

for siblin in bsobj.find("table",{"id":"giftlist"}).tr:
    print siblin

