import requests # for specialised http requests
import urlparse  # for parsing http / https
import collections # implements specialised container datatypes
import os # retrieves current working directory
from lxml import html # used for parsing specific html elements  

# Chosen seed url
seed = 'https://gocardless.com'

def crawl(seed):
    usr_input = str(raw_input("Would you like to crawl the following domain: " + seed + " (y/n): ")).lower().strip()
    if usr_input[0] == "y":
        
        # Variables for both collections & request modules
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

            # Get Response from url data structure at 0 and set timeout to 10 seconds
            response = requests.get(url)

            # If Bad Request then break
            if (response.status_code == 400 or response.status_code == 403 or response.status_code == 404) : 
                print "Bad Request"
                break 
            
            # Print Response Header information
            print "---------------------- SUCCESSFUL REQUEST ----------------------","\n","\n".join("\n {}: {}".format(k, v) for k, v in response.headers.items())
            
            # Capture and Parse HTML body elements
            parsed_body = html.fromstring(response.content)

            # Parse all html hyperlinks
            links = {urlparse.urljoin(response.url, url) for url in parsed_body.xpath('//a/@href') if urlparse.urljoin(response.url, url).startswith('https://gocardless.com/')}

            length = len(links)

            # Amount of Links found
            print "\n" + "---------------------- CRAWLING ----------------------","\n","\n"  
            
            # Set difference to find new URLs
            for link in (links - fetched_domains):
              fetched_domains.add(link)
              queue.append(link)
            
            print("\n".join(fetched_domains))
            # Amount of Links found
            print "\n" + "---------------------- TOTAL LINKS ----------------------","\n","\n" + "No. of Links: " + str(length) + "\n"  
            # Stop after timeout
            break

    if usr_input[0] == "n":
        print "Exiting Program..."
        exit()
    else:
        return output(fetched_domains)


def output(result):
    rooturl = os.getcwd()
    usr_input = str(raw_input("Confirm the following $PATH to export results :" + "\n" + rooturl +   
        "\n" + "To continue please choose (y/n): ")).lower().strip()
    if usr_input[0] == "y":
        try:
            fout = open('results.txt', 'w')
        except:
            print('File cannot be opened:', fname + '.txt')
            exit()
        export = str(result)
        fout.write(export)
        print 'The following web crawler results have been exported to: ' + rooturl + '/results.txt'
    
    if usr_input[0] == "n":
        print "Exiting Program..."
        exit()

# Begin our callback logic     
crawl(seed)