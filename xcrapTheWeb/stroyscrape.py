from bs4 import  BeautifulSoup
from urllib2 import *

html= urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsobj = BeautifulSoup(html.read())

print bsobj
print

newtext = [bsobj.findAll("span",{"class":"green"}),bsobj.findAll("span",{"class":"red"})]


print [item.get_text() for item in bsobj.findAll({"h1","h2","h3","h4"})]

for i in newtext:
    print("*"*100)

    for item in i:
        print item.get_text()