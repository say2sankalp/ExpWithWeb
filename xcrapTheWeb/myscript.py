import  urllib2
from bs4 import  BeautifulSoup


try:

    html = urllib2.urlopen("http://www.pythonscraping.com/pages/page1.html")

    bsObj =BeautifulSoup(html.read())


    l= [
        bsObj.html.body.h1,
    bsObj.body.h1,
    bsObj.html.h1
    ]

    for i in l:
        print "*"*55
        print i

except HTTPError as e:

    print e