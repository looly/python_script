#!/usr/bin/env python
# -*-coding:utf8-*-

import urllib2
import re
import os

CHARSET = 'GBK'
BASE_URL = 'http://www.jj20.com'
LOCAL_DIR = '/opt/temp/img/'

#查找分类
def findCategoryUrl():
    content = urllib2.urlopen('http://www.jj20.com/').read().decode(CHARSET)
    allLink = re.findall(r'<li ><a href="(.*?)">(.*?)</a>', content)
    resultArray = [(BASE_URL + linkTuple[0], linkTuple[1]) for linkTuple in allLink];
    #[(种类URL，种类名字)]
    return resultArray

#查找图片种类
def findPicClass(categoryUrl, name):
    content = urllib2.urlopen(categoryUrl).read().decode(CHARSET)
    allLink = re.findall(r'<a href="(.*?)">(.*?)</a>.*?<ins>.*?</ins>', content)
    resultArray = [(BASE_URL + linkTuple[0], name + '/' + linkTuple[1]) for linkTuple in allLink];
    #[(图片种类URL，种类路径)]
    return resultArray

#下载图像
def downloadImg(imgUrl, localDir):
    try:
        res = urllib2.urlopen(imgUrl)
    except urllib2.HTTPError as e:
        print('Error to request [' + imgUrl + '], code: ' + e.code)
    
    os.makedirs(localDir)
    fileName = imgUrl[imgUrl.rfind('/')+1:]
    f = open(localDir + fileName, 'w')
    f.write(res.read())

if __name__ == '__main__':
    #downloadImg('http://www.jj20.com/down.php?p=/up/allimg/811/101314111I6/141013111I6-0.jpg', '/opt/test/img/')
    allLink = findCategoryUrl()
    for linkTuple in allLink:
        link,name = linkTuple
        allPicClass = findPicClass(link, name)
        for picClass in allPicClass:
            picLink,picName = picClass
            print picLink + ' ' + picName
