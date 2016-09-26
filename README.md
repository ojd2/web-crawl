# Py-Crawl

Implementing a web crawler from first principles. 

### Task:

Generate a Web Crawler to extract elements and build a simple Sitemap.

### Compile & Installation

#### Modules

The following modules have been used in the following web crawling program:

- `Queue`
- `sys`
- `time`
- `urllib2`
- `urlparse`
- `BeautifulSoup`

These can be installed individually or by running the following Python module install command from within the project root folder:

```
python setup.py
```

#### Compile

To compile the program, simply return the following in your terminal, ensuring the latest version of Python is installed:

```
python CRAWLER.py
```

### Introduction & Implementation Research:

Web crawler programs are used to scan and parse HTML webpages to return hyperlinks or any other kind of specific HTML document markup. Web crawlers (also known as web spiders) are simple on paper but tremendously tricky in implementation. Overtime, web crawlers have utilised various information retrieval algorithms for industry use, for example, Google and Mircosoft deploy many isolated web crawlers across multiple distributive architectures to maximise many different web crawling techniques.

Subsequently, these techniques are combined with other isolated components to form a total web crawling application such as Google's homepage exhibits. Behind the scenes, there is a GUI, an independent Parser, various Web Crawler Algorithms and a robust Database to store any relevant retrieval request or storage meta information.   

Overtime, web crawlers have been built for a variety of different tasks, however, the most common are the following:

- To test and check for valid HTML markup hyperlinks on a webpage
- To monitor site maps for administrative tasks and content changes
- To search for hidden and potentially threatening HTML markup content
- To build a collection of extracted media such as HTML markup images and links

All of these have seen substantial growth since the early implementations of web crawlers. As a result, it has been documented by various sources, that the following algorithms listed below are key to the success of crawler implementations and application:

- Breadth first crawling
- Depth first crawling
- Repetitive crawling
- Targeted crawling
- Deep web crawling


#### Breadth First Crawling Algorithm

Breadth First crawling utilises the data structure of a 'queue', fetching and storing pages as it traverses from "lowest level in the in a graph" to then conducting an comparative analysis of the lowest level by "then checking neighbour nodes step by step" (Patel & Jethva, 2015) until the whole graph has been traversed. Essentially, the Breadth First Crawling algorithm is handy for relative URL fetching. For example, there may be a seed, to which the seed (our chosen root url to search) starts with a 'www'. For every other hyperlink found, it traverses through a graph of nodes (found hyperlinks) and compares each node step by step. 

#### Depth First Crawling Algorithm

The Depth First Crawling algorithm utilises the data structure of a 'stack', to which, pages are fetched and traversed from the highest level first. However, "those level" and "relevant neighbour pages" are also fetched and traversed (if there are any) in conjunction. Once this has been executed, the crawler begins to decrement and traverse "into lower level for fetching pages step by step" (Patel & Jethva, 2015).

#### Repetitive Crawling Technique

At a first glance, the repetitive algorithm for web crawling seems self explanatory. A page is fetched from a seed and then hyperlinks are extracted and stored in memory using a crawling algorithm. In many real world use cases, the Repetitive technique is used to keep sitemap indexes up to date. The automation is then repeated over and over again "periodically" overtime. Such implementations of the algorithm + technique of Repetitive Crawling can be found within CMS systems. These are usually integrated into the CMS to capture and fetch any new HTML markup content published on various pages throughout a users website lifetime. 


#### Targeted Crawling

Targeted Crawling is a technique that also utilises the Breadth or Depth First crawling algorithms but this time, instead of fetching HTML markdown hyperlinks from a seed, its "main objective is to retrieve the greatest number of pages relating to a particular subject by using the Minimum Bandwidth" (Patel & Jethva, 2015). This has been commonly integrated into search engine optimisation heuristics. For example, users may want to search a seed and find references to a particular keyword or attribute.

## The Crawler Architecture

Volume handle (Usually handled via a depth level)
Selection Policy (Usually handled via a seed and desired anchor fetcher)
Re-visit Policy (Mechanism to check for changes and when to revisit HTML pages)
Politeness Policy (Handle overloading via a request Timeout)
Parrallelisation (Distributed crawlers but this is for another day...)

#### Fetching

In most cases, the fetching components control the the following:

- Fetching 
- Pipeline and exception handling
- Controlling the flow Http Requests

#### Parsing

The parsing component of a web crawler is vital to its success. The parser usually implements the information retrieval algorithms for searching and traversing through HTML markup to find and locate specific content.

Various information retrieval algorithms are more superior than the other in terms of execution and analysis, however, overall, they all help towards:

	- Stop listing 
	- Stemming
	- URL extraction 
	- HTML Tag trees 
	- URL normalisation

## Task Implementation 

### Why Python?

Based on the research identified above, the following implementation has been conducted in Python. Reasons for using Python revolve around its small vocabulary (reserved words) that make the process of implementing algorithms more natural as a posed to other imperative scripting languages like JavaScript or PHP. 

For example, the following reserved words are included in the Python language:

```
and       del       global      not       with
as        elif      if          or        yield
assert    else      import      pass      
break     except    in          raise
class     finally   is          return
continue  for       lambda      try
def       from      nonlocal    while    

```
As a result, it can make the implementation of programming algorithms more conversing in many aspects. For example, the following psuedo code can be implemented into Python with surprising ease, without any additional esoteric learning:

```
DFS(u):
 Mark u as 'Explored' and ad u to R
 For each edge(u,v), incident to u
 	If v is not marked 'Explored' then
 		Recursively invoke DFS(v)
 	End if
 End for
```
Much of this is down to Pythons reserved keywords, condoning many fundamental similarities with such pseudo code. 

In addition to Pythons easy syntactical sugar and natural reserved keywords, Python also offers a fantastic array of external modules to help with Http Requests. In other languages such as JavaScript, it has only been up until recently, that efficient forms and means of Http request communication has been reinforced to a more accurate degree. Furthermore, the implementation of such modules are easy to integrate and additional tools for communicating directly within the computer operating system using I/O is very diverse in comparison to JavaScript. 

### Let's begin!

An in depth analysis of the program and its implementation has been conducted and can be found below.

#### Program Architecture

Following Program Crawls url(s) from the seed domain and traverses through. It then presents a fetched url and its associated html page title and any unwanted external url(s). This is then passed onto a print function to display the found and crawled url(s) and matches to the command GUI. The idea is to crawl using BFS and present any hierarchical site map distinctions. Such as, all the found url(s) from the seed, and then any external likes. The depth level can be adjusted to go deeper, however, this may present problems in execution and performance.

The program composition is a series of nested block function structures that individually recall each other recursively. This way, the BFS algorithm could utilise several components in isolation. The following program architecture looks like the following:

```
crawl():
  code...

getLinks():
  code...

exCheck():
  code...

exData():
  code...

printMatch():
  code...
```

The architecture follows a simple waterfall sequence, with a majority of the heavy lifting being conducted within the `crawl()` function. This function is called first.

#### The `crawl()` function

Here, a simple BFS information retrieval algorithm is conducted and the construction of the algorithm uses only a few specific types, most notably the `seed` variable, that stores a string containing our chosen root domain to perform the BFS algorithm upon. After a series of confirmation I/O messages displayed to the user, the BFS algorithm begins by exploring outwards from the `seed` domain url in all possible directions. For each `<a>` found within the root html, the `<a>` html tags are further explored and stored into an empty array, utilising a queue and a graph data structure. 

![Image of simple BFS from seed outwards](http://interactivepython.org/runestone/static/pythonds/_images/bfs1.png)

Source: interactivepython.org

Using a queue is very helpful in ensuring that there are no duplicate `<a>` html tags stored into the empty array. Overtime, a series of `<a>` html tags are stored and their inputs are extracted and converted to a string type. Subsequently, a tree like structure of urls are formed, beginning at the seed and outwards and onwards from there. This generates a very simple and verbose sitemap of a website. 

The program begins with the BFS structure firmly intact and some global variables are created:

```
seed = 'http://gocardless.com'

depth_limit = 2

found_urls = []
queue = Queue.Queue()
queue.put(seed)

current_level = 1
```
The `depth_limit` is used for informing the BFS algorithm how deep we would like to perform the iterative traversal search. The context of the word 'deep' in particular, refers to how many layers we would like to explore the website and how far we wish to explore outwards from the `seed`. The `current_level` variable is used to ensure whether a particular level has been searched already or not. 

The `found_urls` is an empty array structure and is used to store all urls found within a single html layer. 

As the BFS algorithm is implemented iteratively, the algorithm uses a Queue like data structure for its exploration. The queue is used to essentially queue all associated urls found into a uniformed level within the graph and to determine which has been explored and which has not...

```
while not queue.empty():
    current_url = queue.get() #retrieve a url from queue
	if current_url not in found_urls:
        found_urls.append(current_url) #if not found, append
        exData(current_url) #function to crawl url html layer
        if current_level != depth_limit:
            current_level = current_level + 1 #compare levels of search
            for link in getLinks(current_url, seed): #extract urls of each url explored
                queue.put(link) # put links into a queue to use later
    print "-" * 80
    else:
        print "Please select a valid option. Either (y/n) please. \n Exiting Program..."
        exit()
```

The code above is rather self explanatory, however, in order to generate more of a sitemap structure, two additional functions are recursively called for each url explored. The two functions called are `exData` and `getLinks`. 

#### The `getLinks()` & `exCheck` functions

The following function simply extracts hyperlink `<a>` data from a single layer of html associated with the explored url. Essentially, the function also double checks to see if url is base url or external and if it finds an external url then the url is passed as a parameter to a function called `exCheck()` to print out the external url and reasons for why it is external.

This particular function grabs any `<title>` tags found in the single layer of Html of the `current_url`:

```
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
```

The `exCheck` function is used to check whether any url found is external. The function simply prints found external links and lists them and as to why they have been deemed as external. The function integrates an comparative analysis / string matcher implementation using a simple array structure. For example, it was noticed early on after one or two tests, that one clear external hyperlink was being found called `support.gocardless.com`. As this url does not follow the same canonical structure of the seed / base url `gocardless.com` - it has been deemed external. This particular function can be scaled upwards, utilising other key html tags such as email addresses, images and any other external information. In addition, it can be very helpful for search engine mechanisms. For now, we are only extracting external urls with the keyword `support`:

```
def exCheck(external_url):
    # Set up an array for external keywords found in url(s) from website
    ignore = ['support']
    # For each item in the ignore list, if external_url matches
    for item in ignore:
        if item in external_url:
            print "-----> Found External URL using keyword: " + item + ":", external_url

```

#### The `exData()` function

The following function is used to extract data from every url that comes up in our BFS crawl algorithm. Using the Beautiful Soup module, we can extract several types of data using certain regular expression patterns from within the underlying module. 

To generate a simple sitemap, we shall just extract the url(s) html `<title>` tags:

```
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
```
The function also calls a `printMatch()` function that is simply used to print any found `<title>` tags to the terminal console.

#### The `printMatch()` function

This function is vital towards the overall GUI and information presentation of the program. It simply prints all matches and associated url(s) found from the BFS traversal function `crawl()`, `getLinks()`, and the `exData()` functions to GUI:

```
def printMatch(title, url, type):
    # As we are passing an array of page titles, go through 
    # each title and clean them up by removing <title> tags.
    # for title_item in title:
    title_matches = title

    # For every page visited, for matches found via bs4 above, print 
    # page titles and the url it has found via the match.
    matching_data = []
    for title in title_matches:
        if title not in matching_data:
            # Add both url and title to matching_data
            matching_data.extend(title)
            if type == "Found Title Page:":
                print " ->", type, title[0]
            else:
                print " ->", type, title.get_text()

```
The resulting waterfall of functions are executed at runtime and recursively present the found information to the user within the terminal. A snippet of the information presented can be found below:

```
Would you like to crawl the following domain: https://gocardless.com (y/n): y
--------------------------------------------------------------------------------
Cool beans! Let's do this!


Crawling in progress...


|-----> Found URL:  https://gocardless.com
 -> Found Page Title: The easiest way to collect recurring payments - GoCardless
 -> Found Page Title: GoCardless
 -> Found Page Title: Check
-----> Found External URL using keyword: support: https://support.gocardless.com
-----> Found External URL using keyword: support: https://support.gocardless.com
|-----> Found URL:  https://gocardless.com/es-es/
 -> Found Page Title: Domiciliación Bancaria simplicada - GoCardless
 -> Found Page Title: GoCardless
 -> Found Page Title: Check
|-----> Found URL:  https://gocardless.com/en-nz/
 -> Found Page Title: New Zealand Direct Debit: Coming Soon - GoCardless
 -> Found Page Title: GoCardless
 -> Found Page Title: Check
```
Once the program has finished executing, in theory, the graph data structure constructed by the `crawl()` BFS algorithm looks like the graph diagram below:

![Image of simple BFS at the final stage](http://interactivepython.org/runestone/static/pythonds/_images/bfsDone.png)

The `seed` url has been explored outwards, and for all the black nodes (found urls) within a single layer of html, these have all been explored recursively, extracting html data and searching for external data, whilst printing the yielded data to the terminal each step of the way.

### Todo List

- Move and construct the program into a `self` manifesting class structure and implementation
- Provide more keywords for the `exCheck` function
- Export found and searched information into file as an xml
- Implement and learn about more core testing methodologies
- Devise a more concise method for extracting additional data 

### References

Patel, J, Jethva, H. (2015). 'Web Crawling'. International Journal of Innovations & Advancement in Computer Science IJIACS. ISSN 2347 8616. Volume 4, Special Issue.

Austwick, J. (2014). 'Python web scraping resource'. Retrieved September 26, 2016, from Python Web Scraping Resources, http://jakeaustwick.me/python-web-scraping-resource/

Duggalrahul, (2016). 'A Web Crawler in Python', Retrieved September 26, 2016, from Web Crawler in Python, https://gist.github.com/duggalrahul/6548584

Miller, B. (2014). 7.9. 'Implementing breadth First search — problem solving with Algorithms and data structures'. Retrieved September 26, 2016, from Interactive Python, http://interactivepython.org/runestone/static/pythonds/Graphs/ImplementingBreadthFirstSearch.html


