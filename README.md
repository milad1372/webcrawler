# Website Link Crawler

This Python program crawls a website and extracts all the unique links from it. The program starts from a given homepage, then follows each link and extracts all links from the subsequent pages. It continues to do this until it has visited a maximum number of pages specified or it has visited all possible pages.

## Requirements

- Python 3.6 or higher

## Dependencies

The project depends on the following Python libraries:

- requests
- BeautifulSoup4

You can install these dependencies using `pip`:

```sh
pip install requests
pip install beautifulsoup4
```sh

## Usage
To use the program, import and call the crawl_website function from your Python script:

```Python
from crawler import crawl_website

start_url = "https://your-website-url.com/"
max_pages = 50
unique_links = crawl_website(start_url, max_pages)

for link in unique_links:
    print(link)
```Python

Replace "https://your-website-url.com/" with the website you want to crawl.

## Important Note
Web scraping should be done ethically and legally. Always ensure that the website you're crawling allows this sort of activity (you can often find this in their "robots.txt" file), and be respectful not to overwhelm their server with too many requests.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT
