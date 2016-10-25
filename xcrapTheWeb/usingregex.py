from bs4 import  BeautifulSoup

from urllib2 import *
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj = BeautifulSoup(html.read())
# f= open('HTMLofpage3.txt','r')
# bsobj =BeautifulSoup(f.readlines())
images = bsobj.findAll("img",{"src",re.compile("\.\./img\/gifts\/img.*\.jpg")})

for image in images:
    print image["src"]
