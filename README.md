![WebSieve](https://github.com/secnextechnologies/WebSieve/blob/main/logo.png)

## Description
"Websieve" is the name of the Python script that extracts unique URLs from a given webpage. It is a combination of the words "web" (referring to the internet) and "sieve" (a tool used to filter out unwanted particles from a mixture). The name suggests that the script is used to filter out All URLs from a webpage and extract only the ones that are unique and relevant.

## Extract Unique URLs from a Webpage

This Python script extracts all unique URLs from a given webpage and outputs them to the console or to a file. It uses the requests module to send a GET request to the specified URL and the BeautifulSoup module to parse the HTML content of the response.

## Installation
1- Install with git:
`` git clone https://github.com/secnextechnologies/WebSieve.git ``

2- Install the required modules: requests, beautifulsoup4, and argparse
* Run `` pip install requests beautifulsoup4 argparse `` to install them

## Options
```
usage: websieve.py [-h] [-u URL] [-c COOKIES] [-o OUTPUT]

Extract unique URLs from a webpage

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     The URL of the webpage to extract URLs from
  -c COOKIES, --cookies COOKIES
                        Cookies to use in the request (optional)
  -o OUTPUT, --output OUTPUT
                        File to save the output to (optional)
```

## How to use
To extract URLs from a webpage, run the script and specify the URL using the -u or --url option:

`` python websieve.py -u https://example.com ``

To save the output to a file, use the -o or --output option:

`` python websieve.py -u https://example.com -o urls.txt ``

You can also specify cookies to use in the request using the -c or --cookies option:

`` python websieve.py -u https://example.com -c "cookie1=value1; cookie2=value2" -o urls.txt ``

## Contribution
#### Pull requests and feature requests are welcomed

## License
WebSieve is released under MIT license. See [LICENSE](https://github.com/secnextechnologies/WebSieve/blob/main/LICENSE).
