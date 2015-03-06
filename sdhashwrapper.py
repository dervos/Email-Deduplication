#! /usr/bin/python2

import md5

from os import listdir
from os.path import isfile, join

path = 'testdata/'
filelist = {}

for f in listdir(path):
    if isfile(join(path, f)):
        filelist[f] = md5.new(open(join(path, f)).read()).digest()


print(filelist)
