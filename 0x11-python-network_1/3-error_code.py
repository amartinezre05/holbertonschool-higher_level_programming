#!/usr/bin/python3
""" displays the body of the response  """
from sys import argv
from urllib import error
from urllib import request


if __name__ == "__main__":
    url = argv[1]

    try:
        with request.urlopen(url) as resp:
            print(resp.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
