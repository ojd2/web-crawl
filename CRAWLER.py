import re
import requests
import httplib
import sys
import os
import time
import Queue
import urllib2
import urlparse
from bs4 import BeautifulSoup

def crawl():
	
	# Set up root domain also known as the seed
    seed = "http://lipsum.com"
    # Confirmation before going any further into hell...
    set_depth = str(raw_input("Would you like to crawl the following domain: " + seed + " (y/n): ")).lower().strip()
    # GET header information...
    print 'hello'

    # Crawl the entire website with no page depth limit
    # Will take a long time for large websites
    if set_depth == "n":
        print "You shall not pass! You are going to be here a while dude?!\n"
        print "Exiting program..."
        exit()

    # Set a crawl web page depth limit
    # Useful for large websites that take a long time to crawl
    elif set_depth == 'y':
    	# For gocardless.com we will go 2, though 1 may be more appropriate and take less time
        depth_limit = 2

        print "-" * 150
        print "Cool beans! Let's do this!\n\n"
        print "Crawling in progress..."

        # Apply the same breadth-first search (BFS) algorithm except in this case
        # We need to to keep track of the depth level and stop the crawl when the
        # Deepest level is reached
        found_urls = []
        queue = Queue.Queue()
        queue.put(seed)
        current_level = 1
        while not queue.empty():
            current_url = queue.get()
            if current_url not in found_urls:
                found_urls.append(current_url)
                exData(current_url)
                if current_level != depth_limit:
                    current_level = current_level + 1
                    for link in getLinks(current_url, seed):
                        queue.put(link)
            time.sleep(1)
        print "-" * 150
    else:
        print "Please select a valid option. Exiting..."
        sys.exit()


# Method to extract all the urls embedded in a web page
# given its url. the base url is also provided as a
# parameter to determine whether the given url is internal
# to the base url and not an external url to another website.
# We are only interested in internal urls. if we follow external
# urls our crawl will never end; however, if we discover external urls
# with either of the words: 'test', 'dev', or 'stage' in them we will
# print that information to the screen.
def getLinks(parent_url, seed):
    child_urls = []
    try:
        opener = urllib2.build_opener()
        opener.addheaders = [("User-agent", "Mozilla/5.0")]
        response = opener.open(parent_url)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")
        # href fields in anchor tags
        anchor_tag_links = soup("a")
        for link in anchor_tag_links:
            if link.has_attr("href"):
                # convert url from a relative path to absolute
                temp_url = urlparse.urljoin(parent_url, link["href"])
                # we're only interested in crawling links in the same domain
                # not external links like facebook, twitter, etc.
                if seed in temp_url:
                    child_urls.append(temp_url)
                else:
                    exCheck(temp_url)
    # http request errors
    except urllib2.HTTPError, e:
        # ignore https errors like 404 - page not found and continue crawling
        pass
    # return a set version of the list to get rid of duplicate urls
    return set(child_urls)


# For urls that are external (not in the base domain) we will not
# crawl them but we will print them to the screen if they have
# one of these words in them: test, dev, or stage because they
# may be of some interest...
def exCheck(external_url):
    if ("fr-fr" in external_url):
        print "-----> Found External URL with the keyword: \'fr-fr\':", external_url
    elif ("fr" in external_url):
        print "-----> Found External URL with the keyword: \'fr-fr\':", external_url
    elif ("se-se" in external_url):
        print "-----> Found External URL with the keyword: \'se-se\':", external_url
    elif ("se" in external_url):
        print "-----> Found External URL with the keyword: \'se\':", external_url
    elif ("support" in external_url):
        print "-----> Found External URL with the keyword: \'support\':", external_url

# A function to extract data from every url that comes up in our BFS crawl
# algorithm. Using regular expressions we can extract several sigs of
# data using certain patterns.
def exData(url):
    #print "Found URL -----> " + url
    # x = url 
    # empty = []
    # empty.append(x)
    # print "Fetched links:" + str(empty)
    try:
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        response = opener.open(url)
        html = response.read()
        #print html
        # get email addresses
        findall(r'([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)', url, html, 'Found Email Address:')
        # get page titles
        findall(r'<title[^>]*>([^<]+)</title>', url, html, 'Found Page Title:')

    except urllib2.HTTPError, e:
        # ignore https errors like 404 - page not found and continue crawling
        pass



# Prints method will print the data found to the screen if there is a match.
def findall(regex, url, html, sig):
    r = re.compile(regex, re.IGNORECASE)
    link_matches = r.findall(html) # recursivley call
    # On every page for each piece of information found we only want to display
    # it once. To do that we keep track of links found using a list.
    matching_data = []
    for link in link_matches:
        if link not in matching_data:
            matching_data.append(link)
            if sig == 'Found Email Address:':
                print 'Found URL -----> ' + url
                print '----->', sig, link[0]
            else:
                print 'Found URL -----> ' + url
                print '----->', sig, link

		#exportData(sig, link)
	
# def exportData(sig,link):
# 	rooturl = os.getcwd()
# 	exporting = str(raw_input("Confirm the following $PATH:" + "\n" + rooturl + "\n" + "To export please select (y/n): ")).lower().strip()
# 	if exporting[0] == "y":
# 		try:
# 			fout = open('crawler-results.txt', 'w')
# 		except:
# 			print('File cannot be opened:', fname + '.txt')
# 			exit()

# 	crawled_data = link,sig # wrong - need to join these two into a list convert to string for exporting
# 	fout.write(crawled_data)
# 	print 'The following web crawler results have been exported to: ' + rooturl + '/crawler-results.txt'
			    
# 	if exporting[0] == "n":
# 	   print "Exiting Program..."
# 	   exit()

#callback
crawl()
