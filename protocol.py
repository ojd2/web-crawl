import requests  
import urlparse  
import collections
from lxml import html
from distutils.util import strtobool  

# Here we have the seed.
seed = 'https://gocardless.com'

queue = collections.deque()  
queue.append(seed)  
fetched_domains = set()  
fetched_domains.add(seed)

print "========================== GO CARDLESS =========================", "\n"


# Do something with response
while len(queue):  
    url = queue.popleft()
    
    # Test to see if domain is less than 1 character long then break
    if len(url) < 1 :
    	print "Invalid url domain"
    	break

    # Get Response from url data structure at 0
    response = requests.get(url)

    # If Bad Request then break
    if (response.status_code == 400 or response.status_code == 403 or response.status_code == 404) : 
    	print "Bad Request"
    	break 
    
    # Print Response Header information
    print "---------------------- SUCCESSFUL REQUEST ----------------------","\n","\n".join("\n {}: {}".format(k, v) for k, v in response.headers.items())
    
    # Capture and Parse HTML body elements
    parsed_body = html.fromstring(response.content)

    # Prints the page title
    #print parsed_body.xpath('//title/text()')

    # Find all links
    links = {urlparse.urljoin(response.url, url) for url in parsed_body.xpath('//a/@href') if urlparse.urljoin(response.url, url).startswith('https://gocardless.com/')}

    length = len(links)

    # Print Responses
    print "---------------------- FOUND LINKS ----------------------",'\n' + "No. of Links: " + str(length) # Amount of links found

    # Set difference to find new URLs
    for link in (links - fetched_domains):
      fetched_domains.add(link)
      queue.append(link)
        
    print("\n".join(fetched_domains))
    