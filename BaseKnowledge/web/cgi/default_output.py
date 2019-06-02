#! /usr/bin/env python3

import cgi
import os
from http import cookies

print('Content-Type: text/html;charset=utf-8')
print('')

if 'HTTP_COOKIE' in os.environ:
  print(os.environ['HTTP_COOKIE'])
  cookie = cookies.SimpleCookie()
  cookie.load(os.environ["HTTP_COOKIE"])
print('Hello, world!')
