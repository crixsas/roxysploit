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
    directory_list = glob.glob('plugins/Exploits/*.plugin')
    for line in directory_list:
        print " " + line.split('plugins/Exploits/')[1].split('.plugin')[0]
    directory_list = glob.glob('plugins/Payloads/*.plugin')
    for line in directory_list:
        print " " + line.split('plugins/Payloads/')[1].split('.plugin')[0]
    directory_list = glob.glob('plugins/Utilities/*.plugin')
    for line in directory_list:
        print " " + line.split('plugins/Utilities/')[1].split('.plugin')[0]

    print ""

def exploits():
    print ""
    print "Plugin Category: Exploits"
    print "====================\n"
    print " Name"
    print " ----"
    directory_list = glob.glob('plugins/Exploits/*.plugin')
    for line in directory_list:
        print " " + line.split('plugins/Exploits/')[1].split('.plugin')[0]
    print " "

def payloads():
    print ""
    print "Plugin Category: Payloads"
    print "====================\n"
    print " Name"
    print " ----"
    directory_list = glob.glob('plugins/Payloads/*.plugin')
    for line in directory_list:
        print " " + line.split('plugins/Payloads/')[1].split('.plugin')[0]
    print " "

def utilities():
    print ""
    print "Plugin Category: Utilities"
    print "====================\n"
    print " Name"
    print " ----"
    directory_list = glob.glob('plugins/Utilities/*.plugin')
    for line in directory_list:
        print " " + line.split('plugins/Utilities/')[1].split('.plugin')[0]
    print " "
