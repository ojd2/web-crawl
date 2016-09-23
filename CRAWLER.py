# ------------------------------------------------------------------------------
# Task:
# ------------------------------------------------------------------------------
# Generate a Web Crawler to extract elements and build a simple Site Map.
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Solution:
# ------------------------------------------------------------------------------
# Following Program Crawls url(s) from the seed domain and traverses through.
# It then presents a fetched url and its associated html page title and any
# unwanted external url(s). This is then passed onto a print function to display 
# the found and crawled url(s) and matches to the command GUI. The idea is to 
# crawl using BFS and present any hierarchical site map distinctions. Such as, 
# all the found url(s) from the seed, and then any external likes. The depth 
# level can be adjusted to go deeper, however, this may present problems in 
# execution and performance.

# Besides this, the implementation of the BFS algorithm is also an educational 
# experiment, to see how Breadth First crawling utilises the data structure of
# 'queues', fetching and storing pages as it traverses from "lowest level in the 
# in a graph" using comparative analysis of the lowest level by 
# "then checking neighbour nodes step by step" (Patel & Jethva, 2015) until 
# the whole graph has been traversed.
# ------------------------------------------------------------------------------
# List imports:
# ------------------------------------------------------------------------------
import Queue
import sys
import time
import urllib2
import urlparse

from bs4 import BeautifulSoup
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Begin Program:
# ------------------------------------------------------------------------------
def crawl():
    # Set up root domain also known as the seed.
    seed = "https://gocardless.com"
    # Confirmation before going any further into hell...
    confirm_depth = str(raw_input("Would you like to crawl the following domain: " + seed + " (y/n): ")).lower().strip()

    # If user selects 'n', then they can safely exit.
    if confirm_depth == "n":
        print "You shall not pass! You are going to be here a while dude?!\n"
        print "Exiting program..."
        exit()

    # Set a crawl depth limit for our BSF algorithm:
    elif confirm_depth == 'y':
        print "-" * 80
        print "Cool beans! Let's do this!\n\n"
        print "Crawling in progress...\n\n"

        # Apply the same breadth-first search (BFS) algorithm except in this case
        # We need to to keep track of the depth level and stop the crawl when the
        # Deepest level is reached. For this particular url we will go with 2.
        depth_limit = 2
        # Set up some BFS variable requirements.
        found_urls = []
        queue = Queue.Queue()
        queue.put(seed)
        current_level = 1
        # Begin the BFS Algorithm...
        while not queue.empty():
            current_url = queue.get()
            if current_url not in found_urls:
                found_urls.append(current_url)
                exData(current_url)
                if current_level != depth_limit:
                    current_level = current_level + 1
                    for link in getLinks(current_url, seed):
                        queue.put(link)
            # Suspend execution for a second.
            time.sleep(1)
        print "-" * 80
    else:
        print "Please select a valid option. Either (y/n) please. \n Exiting Program..."
        exit()

# ------------------------------------------------------------------------------
# Here we fetch all hyperlinks embedded in the crawled base url. 
# Function also double checks to see if url is base url or external
# if it finds an external url then the url is passed as a parameter
# to a function called exCheck() to print out the external url and
# reasons for why it is external.
# ------------------------------------------------------------------------------
def getLinks(parent_url, seed):
    child_urls = []
    try:
        opener = urllib2.build_opener()
        opener.addheaders = [("User-agent", "Mozilla/5.0")]
        response = opener.open(parent_url)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")
        # Find all <a> tags
        anchor_tag_links = soup("a")
        for link in anchor_tag_links:
            if link.has_attr("href"):
                # Convert url from a relative path to absolute by joining 
                # both parent and found link href address.
                temp_url = urlparse.urljoin(parent_url, link["href"])
                # If seed url is found in the temp_url, then great!
                # If not, then send off the temp_url to the exCheck()
                # function to then display why it was detected.
                if seed in temp_url:
                    child_urls.append(temp_url)
                else:
                    exCheck(temp_url)

    # Some HTTP Request Errors may pop up! 
    except urllib2.HTTPError, e:
        # If Error like 404 is requested, continue onwards...
        pass

    # Else, if not, continue on and return a set version of the list 
    # to get rid of duplicate url(s) crawled already.
    return set(child_urls)

# ------------------------------------------------------------------------------
# Any url(s) found to be external, we shall list them and list why
# they have been deemed as external. So let's check them.
# ------------------------------------------------------------------------------
def exCheck(external_url):
    # Set up an array for external keywords found in url(s) from website
    ignore = ['support']
    # For each item in the ignore list, if external_url matches
    for item in ignore:
        if item in external_url:
            print "-----> Found External URL using keyword: " + item + ":", external_url

# ------------------------------------------------------------------------------
# A function to extract data from every url that comes up in our BFS crawl
# algorithm. Using regular expressions we can extract several types of
# data using certain regular expression patterns. To generate a simple site 
# map, we shall just extract the url(s) html <title> tags.
# ------------------------------------------------------------------------------
def exData(url):
    print "|-----> Found URL: ", url
    try:
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        response = opener.open(url)
        html = response.read()
        # Now parse any page title tags...
        soup = BeautifulSoup(html, "lxml")
        title = soup.find_all('title')
        # Send any page titles to the printMatch() with the parent url...
        printMatch(title, url, 'Found Page Title:')

    # If HTTP Request error here, then continue onwards again...
    except urllib2.HTTPError, e:
        pass

# ------------------------------------------------------------------------------
# Print all matches and associated url(s) found to GUI.
# ------------------------------------------------------------------------------
def printMatch(title, url, type):
    # As we are passing an array of page titles, go through 
    # each title and clean them up by removing <title> tags.
    # for title_item in title:
    title_matches = title

    # For every page visited, for matches found via regex above, print 
    # page titles and the url it has found the match.
    matching_data = []
    for title in title_matches:
        if title not in matching_data:
            # Add both url and title to matching_data
            matching_data.extend(title)
            if type == "Found Title Page:":
                print " ->", type, title[0]
            else:
                print " ->", type, title.get_text()
# ------------------------------------------------------------------------------
# Callback our Crawler
# ------------------------------------------------------------------------------
crawl()

# ------------------------------------------------------------------------------
# References:
# ------------------------------------------------------------------------------

# [1] Jitali Patel, Hardik Jethva, "Web Crawling". 2015. 
# [2] IJIACS. ISSN 2347 8616. Volume 4, Special Issue.
# [3] http://jakeaustwick.me/python-web-scraping-resource/#requests
# [4] https://gist.github.com/duggalrahul/6548584