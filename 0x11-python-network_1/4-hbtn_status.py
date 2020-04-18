#!/usr/bin/python3
""" fetches URL """
import requests


if __name__ == "__main__":
    call = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(call.text))
    print('\t- content: {}'.format(call.text))
