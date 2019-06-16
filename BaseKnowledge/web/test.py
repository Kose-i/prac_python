#!/usr/bin/python3
import requests

url = 'https://www.google.com'
#params = {
#    'foo': 123,
#}

#req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode()))
req = requests.get(url)
print(req.text)
with req as res:
    print(res.read())
#with urllib.request.urlopen(req) as res:
#    body = res.read()
