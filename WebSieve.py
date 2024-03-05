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
       				- SecneX Technologies
       				
[INF] Current WebSieve version v1.2
""")

# Set up command line arguments
parser = argparse.ArgumentParser(description="Extract unique URLs from a webpage")
parser.add_argument("-u", "--url", help="The URL of the webpage to extract URLs from")
parser.add_argument("-c", "--cookies", help="Cookies to use in the request (optional)")
parser.add_argument("-o", "--output", help="File to save the output to (optional)")

# Parse command line arguments
args = parser.parse_args()

# Check if URL is provided
if not args.url:
    parser.print_help()
    exit()

try:
    # Convert cookies string to a dictionary
    cookies_dict = {}
    if args.cookies:
        for cookie in args.cookies.split("; "):
            key, value = cookie.split("=")
            cookies_dict[key] = value

    # Convert cookies dictionary to a RequestsCookieJar object
    cookies = cookiejar_from_dict(cookies_dict)

    # Send request and extract URLs
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(args.url, headers=headers, cookies=cookies)
    response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404)
    
    soup = BeautifulSoup(response.content, "html.parser")
    urls = set()  # use a set to store unique URLs

    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith("http"):
            urls.add(href)

    url_list = "\n".join([url for url in urls])
    print(url_list)

    # Output or save the result
    if args.output:
        with open(args.output, "w") as f:
            f.write(url_list)
            print(f"\nURLs saved to {args.output}")
    else:
        print(url_list)

except requests.exceptions.RequestException as e:
    print(f"Error: {str(e)}")
