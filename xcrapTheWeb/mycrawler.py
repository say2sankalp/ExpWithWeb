from bs4 import BeautifulSoup
from urllib2 import *
import  datetime
import random
import re


def get_links(url):
    global pages
    html = urlopen("http://en.wikipedia.org"+url)
    bsobj= BeautifulSoup(html.read())
    link_pages=  bsobj.find("div",{"id":"bodyContent"})\
        .findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
    return link_pages


links = get_links("/wiki/Attention_deficit_hyperactivity_disorder")
print type(links)


while len(links) >0:
    newarticle= links[random.randint(0,len(links)-1)].attrs['href']
    print newarticle
    links= list(set(get_links(newarticle)))