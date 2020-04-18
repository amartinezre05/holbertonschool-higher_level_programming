#!/usr/bin/python3
""" request to the URL and displays the value of the variable X-Request-Id """
import requests
from sys import argv


if __name__ == "__main__":
    call = requests.get(argv[1])
    head = call.headers.get('X-Request-Id')
    print(head)
