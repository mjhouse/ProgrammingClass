#!/usr/bin/env python

import requests

STARTING_URL = "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token"

def print_hello():
    print("HELLO")

def show_data_types():
    int_type   = 7
    float_type = 1.3
    str_type   = "this is text"
    func_type = print_hello

    list_type  = [ 'A', 'B', 0, 0.0 ]
    dict_type  = { 'A': 'WHATEVER', 'B': 0 }

    ## NUMBERS
    # print(int_type)
    # print(float_type)

    ## STRINGS
    # print(str_type)

    ## LISTS
    # print(list_type[1])

    ## DICTIONARY
    # print(dict_type['B'])
    # dict_type['B'] = print_hello
    # dict_type['B']()

def get_page_text( url_to_download ):
    page = requests.get(url_to_download)
    text = page.text
    return text

def main():
    text = get_page_text(STARTING_URL)
    split_text = text.split('\n')

    length_of_list = len(split_text)
    print(length_of_list)

    # for line in split_text:
    #     print(line)

if __name__=='__main__':
    main()