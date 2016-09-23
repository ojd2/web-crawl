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

# Begin Program:
def crawl():
	# Set up root domain also known as the seed
    seed = "http://lipsum.com"
    # Confirmation before going any further into hell...
    confirm_depth = str(raw_input("Would you like to crawl the following domain: " + seed + " (y/n): ")).lower().strip()
    
    
    # Crawl the entire website with no page depth limit
    # Will take a long time for large websites
    if confirm_depth == "n":
        print "You shall not pass! You are going to be here a while dude?!\n"
        print "Exiting program..."
        exit()

    # Set a crawl web page depth limit
    elif confirm_depth == 'y':

    	# For gocardless.com we will go 2, though 1 may be more appropriate and take less time
        depth_limit = 2

        print "-" * 80
        print "Cool beans! Let's do this!\n\n"
        print "Crawling in progress...\n\n"

        # Apply the same breadth-first search (BFS) algorithm except in this case
        # We need to to keep track of the depth level and stop the crawl when the
        # Deepest level is reached:
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
        print "-" * 80
    else:
        print "Please select a valid option. Exiting..."
        sys.exit()


# Here we fetch all hyperlinks embedded in the crawled base url. 
# Function also double checks to see if url is base url or external
# if it finds an external url then the url is passed as a parameter
# to a function called exCheck() to print out the external url and
# reasons for why it is external.
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
    # to get rid of duplicate urls crawled already.
    return set(child_urls)


# Any urls found to be external, we shall list them and list why
# they have been deemed as external.
def exCheck(external_url):
	# Set up an array for external keywords found in urls from website
	ignore = ['support']
	# For each item in the ignore list, if external_url matches
	for item in ignore:
		if item in external_url:
			print "-----> Found External URL using keyword: " + item + ":", external_url 


# A function to extract data from every url that comes up in our BFS crawl
# algorithm. Using regular expressions we can extract several types of
# data using certain regular expression patterns.
def exData(url):
 	print "-----> Found URL: ", url
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

        	exp_title = str(title).strip("[]")
    		exp_url = str(url)
    		export = "\n" + "\n".join([exp_url, exp_title]) + "\n"

    		final_export = list(export) # However, keep each item added, not overwrite?
    		#print export

        # If HTTP Request error here, then continue onwards again...
    	except urllib2.HTTPError, e:
        	pass

# Print all matches found to GUI
def printMatch(title, url, type):
    # As we are passing an array of page titles, go through 
    # each title and clean them up by removing <title> tags.
    #for title_item in title:
    title_matches = title
    
    # For every page visited, for matches found via regex above, print 
    # page titles and the url it has found the match.
    matching_data = []
    for title in title_matches:
        if title not in matching_data:
            matching_data.append(title)
            if type == "Found Title Page:":
                print " ---->", type, title[0]
            else:
            	print " ---->", type, title.get_text()
    
    
    

    # Here, I wish to take each item and push this into another data structure to 
    # write the data and export to file...
    


		#exportData(sig, link)
	
#def exportData(data):



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

# Callback
crawl()
