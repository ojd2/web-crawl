# Py Crawl Web Crawler

Implementing a web crawler from first principles.

### Task:

We'd like you to write a simple web crawler (without the use of frameworks such as scrapy, anemone etc), in whatever language you're most comfortable in, which given a URL to crawl, should output a site map, showing the static assets for each page. We'd love it if you could also include a README file which explains your design decisions and any parts you found particularly challenging or interesting.

However, a regular expression or some sort of implementation must be integrated. The crawler will be used on gocardless.com and should not return any links without 'gocardless' within its canonical form. So for example, the crawler should exclude twitter or facebook links.

 ### Introduction and background:

Web crawler programs are used to scan and parse HTML webpages to return hyperlinks or any other kind of specific HTML document markup. Web crawlers (also known as web spiders) are simple on paper but tremendously tricky in implementation. Overtime, web crawlers have had to utilise various information retrieval algorithms and architectures for industry use, for example, Google and Mircosoft deploy many isolated web crawlers across multiple distributive architectures to maximise many different web crawling techniques.

Subsequently, these techniques are combined with other isolated components to form a total web crawling application such as Google's homepage exhibits. Behind the scenes, there is a GUI, an independent Parser, various Web Crawler Algorithms and a finally a robust Database to store any relevant request or storage meta.   

Overtime, web crawlers are built for a variety of different tasks, however, the most common are the following:

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

Volume handle (number of pages fetched - how to handle this?)
Selection Policy (a mechanisim to state which page to download?)
Re-visit Policy (a mechanisim to check for changes and when to revist HTML pages)
Politeness Policy (Handle overloading of content)
Parrallelisation (How to crawl web pages across large networks?)

#### Fetching


Fetching, pipeline and exception handling from http requests.

#### Parsing

Task of simply finding and traversing through HTML markup to find and locate content.

Within Parsing we also have the following components:

	- Stop listing 
	- Stemming
	- URL extraction 
	- HTML Tag trees 
	- URL normalisation

TBC....












References
----------

Jitali Patel, Hardik Jethva, "Web Crawling". 2015. International Journal of Innovations & Advancement in Computer Science IJIACS. ISSN 2347 8616. Volume 4, Special Issue.


Hyperlinks:

http://jakeaustwick.me/python-web-scraping-resource/#requests

https://gist.github.com/duggalrahul/6548584


