import requests
from bs4 import BeautifulSoup
import argparse
from requests.utils import cookiejar_from_dict

# Banner
print("""
 __      __      ___.     _________.__                    
/  \    /  \ ____\_ |__  /   _____/|__| _______  __ ____  
\   \/\/   // __ \| __ \ \_____  \ |  |/ __ \  \/ // __ \ 
 \        /\  ___/| \_\ \/        \|  \  ___/\   /\  ___/ 
  \__/\  /  \___  >___  /_______  /|__|\___  >\_/  \___  >
       \/       \/    \/        \/         \/          \/ 
       				- SecneX Technologies (secnex.tech)
       				
[INF] Current WebSieve version v1
""")

# Set up command line arguments
parser = argparse.ArgumentParser(description="Extract unique URLs from a webpage")
parser.add_argument("-u", "--url", help="The URL of the webpage to extract URLs from")
parser.add_argument("-c", "--cookies", help="Cookies to use in the request (optional)")
parser.add_argument("-o", "--output", help="File to save the output to (optional)")

# Parse command line arguments
args = parser.parse_args()

# Convert cookies string to a dictionary
cookies_dict = {}
if args.cookies:
    for cookie in args.cookies.split("; "):
        key, value = cookie.split("=")
        cookies_dict[key] = value

# Convert cookies dictionary to a RequestsCookieJar object
cookies = cookiejar_from_dict(cookies_dict)

# Send request and extract URLs
response = requests.get(args.url, cookies=cookies)
soup = BeautifulSoup(response.content, "html.parser")
urls = set() # use a set to store unique URLs

for link in soup.find_all('a'):
    href = link.get('href')
    if href and href.startswith("http"):
        urls.add(href)

#url_list = "\n".join([f"{index+1}. {url}" for index, url in enumerate(urls)])
url_list = "\n".join([url for url in urls])
print(url_list)

# Output or save the result
if args.output:
    with open(args.output, "w") as f:
        f.write(url_list)
        print(f"\nURLs saved to {args.output}")
else:
    print(url_list)
