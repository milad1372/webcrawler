"""
By: Milad Momeni
This Python script crawls a given website and extracts all unique links up to a maximum
number of pages. The program then outputs all unique links found.

"""
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_website(start_url, max_pages):
    # List of pages we need to crawl
    pages_to_crawl = [start_url]
    # Set of already crawled pages
    crawled_pages = set()
    # Set of unique links found on the crawled pages
    unique_links = set()

    # Loop until we have crawled the maximum pages or there are no more pages to crawl
    while pages_to_crawl and len(crawled_pages) < max_pages:
        # Get the next page URL from the list
        page_url = pages_to_crawl.pop(0)

        try:
            # Send a GET request to the page
            response = requests.get(page_url, timeout=5)
            # If the GET request is not successful, raise an exception
            response.raise_for_status()
        except (requests.RequestException, ValueError):
            # If an error occurs, skip this page and continue with the next one
            continue

        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Add the page to the set of crawled pages
        crawled_pages.add(page_url)

        # Find all the 'a' tags (links) in the page
        for link in soup.find_all('a'):
            # Get the URL from the 'href' attribute
            url = link.get('href')
            if url:
                # Convert the URL to an absolute URL
                absolute_url = urljoin(start_url, url)
                # If this URL has not been crawled yet, add it to the list of pages to crawl
                if absolute_url not in crawled_pages:
                    pages_to_crawl.append(absolute_url)
                    unique_links.add(absolute_url)

    # Return the set of unique links found
    return unique_links

# Update max_pages to the desired maximum number of pages to crawl
start_url = "https://ussu.ca/"
max_pages = 50
unique_links = crawl_website(start_url, max_pages)

# Print all the unique links
for link in unique_links:
    print(link)
