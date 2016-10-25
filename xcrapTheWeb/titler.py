import  urllib2

from bs4 import  BeautifulSoup

from urllib2 import  HTTPError

def getitle(url):

    try:
        html = urllib2.urlopen(url)

    except HTTPError as e:
        return e

    try:
        bsobj= BeautifulSoup(html.read())
        title = bsobj.body.h1

    except AttributeError as e:
        return  None

    return  title

title= getitle("http://www.pythonscraping.com/pages/page1.html")
if title is None:
    print "Title could be found"
else:
    print  title
    print  

