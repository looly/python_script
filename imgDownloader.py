#!/usr/bin/env python
# -*-coding:utf8-*-
#
# Author：Looly
# 用于批量下载图片

import sys
import os

import urllib
import hashlib

#----------------------------------------------------
#保存到本地文件的扩展名
EXT = '.jpg'
#本地保存路径
DIR = './images'
#----------------------------------------------------

def readUrls(path):
    '''读取url列表'''
    with open(path) as file:
        return file.readlines()

def checkFile(finishedBlock, blockSize, totalSize):
    '''检查下载进度'''
    finishedSize = finishedBlock * blockSize;
    if finishedSize > totalSize: finishedSize = totalSize;
    percent = 100 * finishedSize / totalSize;
    print('%.2f%%, Finished: %s, total: %s' % (percent, finishedSize, totalSize))

def buildPath(url, dir):
    '''构建本地路径'''
    if '' == dir:
        dir = './'
    elif '/' != dir[-1]:
        dir = dir + '/'
    fileName = hashlib.md5(url).hexdigest() + EXT
    #采用三级目录存储，按照MD5值的第一个和第二个字符分目录
    dir = dir + fileName[0] + '/' + fileName[1] + '/'
    mkdirs(dir)
    return dir + fileName

def download(url, dir=DIR):
    '''下载'''
    path = buildPath(url, dir)
    print('Save file to ' + path)
    ##TODO 这个方法在遇到非法路径时会抛出异常，对404页面无法识别，后续改进
    urllib.urlretrieve(url, path, checkFile)

def start():
    '''启动服务'''
    if len(sys.argv) < 2 or '' == sys.argv[1]:
        print('ERROR: Please provide url path as first argument!')
        return
    path = sys.argv[1]
    
    for line in readUrls(path):
        line = line.strip()
        print('Download ' + line)
        download(line)

def mkdirs(path):
    '''创建逐层目录，忽略已存在的目录'''
    if not os.path.exists(path):
        os.makedirs(path)

#主入口
if __name__ == '__main__':
    start()
