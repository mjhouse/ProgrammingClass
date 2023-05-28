#!/usr/bin/env python

import requests

STARTING_URL = "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token"



def get_page_text(url_to_download):
    page = requests.get(url_to_download)
    text = page.text
    return text


def main():
    text = get_page_text(STARTING_URL)
    print(text)
#     page = requests.get(STARTING_URL)
    
#     print(page.text)
#     print(page.status_code)


if __name__=='__main__':
    main()