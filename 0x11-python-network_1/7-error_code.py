#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response """
import requests
from sys import argv


if __name__ == "__main__":
    if requests.get(argv[1]).status_code >= 400:
        print('Error code:', requests.get(argv[1]).status_code)
    else:
        print(requests.get(argv[1]).text)
