#!/usr/bin/env python

import glob
import sys
import os

def all():
    print ""
    print "Plugin Category: All"
    print "====================\n"
    print " Name"
    print " ----"
    directory_list = glob.glob('plugins/*.plugin')
    for line in directory_list:
        print " " + line.split('plugins/')[1].split('.plugin')[0]
