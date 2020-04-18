#!/usr/bin/python3
""" takes in a URL and an email address, sends a POST request """
import requests
from sys import argv


if __name__ == "__main__":
    data = {'email': argv[2]}
    print(requests.post(argv[1], data=data).text)
