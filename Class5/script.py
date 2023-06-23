#!/usr/bin/env python

import requests
import bs4

STARTING_URL = "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token"

def crawl(initial):
    # add it to our stack
    stack = [ initial ]
    visited = []

    # loop while stack not empty
    while stack:

        # get the top url off the stack
        url = stack.pop()
        print(f"crawling {url}")

        # check to see if it's been visited
        if url in visited:
            continue

        visited.append(url)

        # fetch the page for the url 
        page = None

        try:
            page = requests.get(url)
        except:
            continue

        if page.status_code != 200:
            continue

        # parse the html of the page
        soup = bs4.BeautifulSoup(page.text)

        # add all links to the stack
        for tag in soup.find_all('a'):
            stack.append(tag.get('href'))

    

if __name__=='__main__':
    crawl(STARTING_URL)