#! /usr/bin/python2

import sys
import md5
import pyzmail
import traceback

from os import listdir
from os.path import isfile, join

path = '/home/dervos/code/Uforia/TESTDATA/'
filelist = {}


for f in listdir(path):
    if isfile(join(path, f)):
        try:
            temp_email = ""
            email_file = open(join(path, f))
            msg = pyzmail.PyzMessage.factory(email_file)
            email_file.close()
            header1 = msg.get_decoded_header("Message-ID", None)
            header2 = msg.get_decoded_header("X-Folder", None)

            emaildict = dict(msg)


            email_file = open(join(path, f))
            for line in email_file.readlines():
                if "X-Folder" in line:
                    print("test")

    #        digest = md5.new().digest()
    #        if digest not in filelist.values():
    #            filelist[f] = digest
        except:
            traceback.print_exc(file=sys.stderr)
