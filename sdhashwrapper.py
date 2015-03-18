#! /usr/bin/python2

import md5
import sys
import traceback

from os import listdir
from os.path import isfile, join

path = 'testdata/'
filelist = {}
DECLUDED_HEADERS = {"X-Folder", "Message-ID"}


def checkHeader(line):
    for header in DECLUDED_HEADERS:
        if header in line:
            return True

for f in listdir(path):
    if isfile(join(path, f)):
        try:
            emailarray = []
            email_file = open(join(path, f))
            for line in email_file.readlines():
                if not checkHeader(line):
                    emailarray.append(line)

            digest = md5.new(''.join(
                    [str(line) for line in emailarray]
                )).digest()
            if digest not in filelist.values():
                filelist[f] = digest
        except:
            traceback.print_exc(file=sys.stderr)

print(filelist)
