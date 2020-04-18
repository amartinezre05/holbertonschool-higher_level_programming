#!/usr/bin/python3
""" displays the body of the response  """
from sys import argv
from urllib.parse import urlopen
from urllib import request


if __name__ == "__main__":
    data = urlencode({
        'email': argv[2]
    }).encode('ascii')
    call = request.Request(argv[1], data)

    with urlopen(call) as resp:
        print("{}".format(resp.read().decode()))