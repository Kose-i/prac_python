#! /usr/bin/env python3

import urllib.request

import pickle

params = {'q':'keyword', 'page':1}
encoded_params = pickle.dumps(params)
print(encoded_params)
urllib.request.urlopen('http://yahoo.co.jp/', data=encoded_params)
