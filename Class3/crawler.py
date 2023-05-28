#!/usr/bin/env python

import requests

STARTING_URL = "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token"

def main():
    page = requests.get(STARTING_URL)
    
    print(page.text)
    print(page.status_code)

if __name__=='__main__':
    main()