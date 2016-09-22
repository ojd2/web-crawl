import requests 
import sys
import queue
import time
import urlib2
import urlparse
from bs4 import beautifulsoup

# Crawler extracts the following information
def crawler():
	print "The following will crawl and extract the following: \n"
	print "Page Titles\n"
	print "URLs\n"

	seed = raw_input("Please enter a valid URL to crawl: ") # insert https://domain.com
	depth_level = 1 # deafult depth level for BFS algorithm

	if depth_level == 0:
		print 'sorry no can do'
		exit()
	if depth_level == 1:
		
	# Next we will define a simple cralwer algorithm using bfs search.
	# In principle, all websites have hyperlinks, with this in mind, our website will be the root. 
	# From the root we have a series of children hyperlinks, these hyperlinks are at level 1.
	# To iterate deeper down past beyond level 1, it's best to implement a BFS algorithim to capture
	# all the childrens children and so on...

	# To begin with, implement empty array for found urls from the root
	found_urls = []
	queue = Queue().Queue()
	queue.put(seed)