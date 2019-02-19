#! /usr/bin/env python3

import urllib.parse

params = {'alpha':'az', 'space':' ', 'num':'19'}
query_string = urllib.parse.urlencode(params)

print(query_string)

