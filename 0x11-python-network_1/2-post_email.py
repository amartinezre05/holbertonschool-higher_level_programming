#!/usr/bin/python3
""" displays the body of the response  """
from sys import argv
from urllib.parse import urlencode
from urllib import request


if __name__ == "__main__":
    data = urlencode({
        'email': argv[2]
    }).encode('utf-8')
    call = request.Request(argv[1], data)

    with request.urlopen(call) as resp:
        print("{}".format(resp.read().decode()))
