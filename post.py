#!/usr/bin/env python
# -*-coding:utf8-*-

import urllib,urllib2

url = 'http://localhost:8090'
params = {'a':'1', 'b':'2', '姓名': '张三'}
data = urllib.urlencode(params)
print('Encoded Data: ' + data)
req = urllib2.Request(url, data)
print('---------------------------')
print(urllib2.urlopen(req).read())
