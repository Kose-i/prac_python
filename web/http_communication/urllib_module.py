#! /usr/bin/env python3

import urllib.request, urllib.error

response = urllib.request.urlopen('http://google.com')

content = response.read()
print(content)

headers = response.info()
print("\ncontent-type:", headers['content-type'])
print("date:", headers['date'])
