import re
import urllib2
#from urllib.parse import urlparse
from sets import Set

seed = 'https://gocardless.com'
url_collection = Set([seed])

def findId(source):
    l = re.findall(r'"((https?):\/\/)?(\w+\.)*(?P<gocardless>\w+)\.(\w+)(\/.*)?"',source)
    return l

def get_source(url):
    response = urllib2.urlopen(url)
    page_source = response.read()
    return page_source

def search(source, depth):
    if depth==2:
        return
    print source, depth

    try:
        page_source = get_source(source)
        links = Set(findId(page_source))
    except:
        print 'some error encountered'
        return

    global url_collection
    for link in links:
        if link not in url_collection:
            url_collection = url_collection|Set([link])        

    for link in url_collection:
        search(link,depth+1)

search(seed,0)

