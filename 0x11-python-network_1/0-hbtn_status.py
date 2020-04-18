#!/usr/bin/python3
""" fetches url """
from urllib import request


if __name__ == "__main__":
    with urlopen('https://intranet.hbtn.io/status') as resp:
        cont = resp.read()
        print('Body response:')
        print('\t- type: {}'.format(type(cont)))
        print('\t- content: {}'.format(cont))
        print('\t- utf8 content: {}'.format(cont.decode()))
