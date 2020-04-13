#!/usr/bin/env python

'''
    File name: macaddress.py
    Description: Retrieves 'Company Name' for a Mac Addresses using macaddress.io API
    Author: Tariq Syed, Accenture
    Date created: 4/8/2020
    Python Version: 3.7+
'''

import requests, argparse

# Use argparse to process arguments.
parser = argparse.ArgumentParser()
parser.add_argument('-k', '--api_key', required=True, help="macaddress.io API key (required)")
parser.add_argument('-m', '--mac_address', required=True, help="Mac Address (required)")
args = parser.parse_args()

apiurl = 'https://api.macaddress.io/v1'
payload = {'search': args.mac_address, 'apiKey': args.api_key}

r = requests.get(apiurl, params=payload)

print('MAC Address:', args.mac_address)
print('Company Name:', r.text)
