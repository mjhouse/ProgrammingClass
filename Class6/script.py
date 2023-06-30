#!/usr/bin/env python

import requests
import bs4
import time
from bloom_filter import BloomFilter

STARTING_URL = "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token"

# 1. We can't kill the crawler (easily)
# 2. The "visited check" gets slower as we crawl

def crawl(initial):
    # add it to our stack
    stack = [ initial ]
    bloom = BloomFilter(max_elements=10000, error_rate=0.1)

    # loop while stack not empty
    while stack:

        # get the top url off the stack
        url = stack.pop()
        print(f"crawling {url}")

        # check to see if it's been visited
        check = False 

        time_before = time.perf_counter_ns()
        check = url in bloom
        time_after = time.perf_counter_ns()

        # print(time_after - time_before)

        if check:
            continue

        bloom.add(url)

        # fetch the page for the url 
        page = None

        try:
            page = requests.get(url)
        except KeyboardInterrupt as e:
            print(e)
            break
        except:
            continue

        if page.status_code != 200:
            continue

        # parse the html of the page
        soup = bs4.BeautifulSoup(page.text,features="lxml")

        # add all links to the stack
        for tag in soup.find_all('a'):
            link = tag.get('href')
            if link:
                stack.append(str(link))

    print("done crawling!")

if __name__=='__main__':
    crawl(STARTING_URL)