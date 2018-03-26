#!/usr/bin/env python

import glob
import sys
import os

def all():
    print ""
    print "Plugin Category: All"
    print "==============================\n"
    print " Name              Description"
    print " ----              -----------"
    directory_list = glob.glob('plugins/Exploits/*.plugin')
    for line in directory_list:
        about = line
        with open(about, 'r') as myfile:
            data = myfile.read().splitlines()
            desc = data[0]
            datar = desc.replace("Description = '", "")
        x = datar.rstrip("'")
        bb = line.split('plugins/Exploits/')[1].split('.plugin')[0]
        if x == "#!/usr/bin/python":
            x = "\033[1;91mDescription has not yet been implemented.\033[1;m"
        print " %s\t   %s" % (bb,x)
    directory_list = glob.glob('plugins/Payloads/*.plugin')
    for line in directory_list:
        about = line
        with open(about, 'r') as myfile:
            data = myfile.read().splitlines()
            desc = data[0]
            datar = desc.replace("Description = '", "")
        x = datar.rstrip("'")
        bb = line.split('plugins/Payloads/')[1].split('.plugin')[0]
        if x == "#!/usr/bin/python":
            x = "\033[1;91mDescription has not yet been implemented.\033[1;m"
        print " %s\t   %s" % (bb,x)
    directory_list = glob.glob('plugins/Utilities/*.plugin')
    for line in directory_list:
        about = line
        with open(about, 'r') as myfile:
            data = myfile.read().splitlines()
            desc = data[0]
            datar = desc.replace("Description = '", "")
        x = datar.rstrip("'")
        bb = line.split('plugins/Utilities/')[1].split('.plugin')[0]
        if x == "#!/usr/bin/python":
            x = "\033[1;91mDescription has not yet been implemented.\033[1;m"
        print " %s\t   %s" % (bb,x)
    print " "

def exploits():
    print ""
    print "Plugin Category: Exploits"
    print "==============================\n"
    print " Name              Description"
    print " ----              -----------"
    directory_list = glob.glob('plugins/Exploits/*.plugin')
    for line in directory_list:
        about = line
        with open(about, 'r') as myfile:
            data = myfile.read().splitlines()
            desc = data[0]
            datar = desc.replace("Description = '", "")
        x = datar.rstrip("'")
        bb = line.split('plugins/Exploits/')[1].split('.plugin')[0]
        if x == "#!/usr/bin/python":
            x = "\033[1;91mDescription has not yet been implemented.\033[1;m"
        print " %s\t   %s" % (bb,x)
    print " "

def payloads():
    print ""
    print "Plugin Category: Payloads"
    print "==============================\n"
    print " Name              Description"
    print " ----              -----------"
    directory_list = glob.glob('plugins/Payloads/*.plugin')
    for line in directory_list:
        about = line
        with open(about, 'r') as myfile:
            data = myfile.read().splitlines()
            desc = data[0]
            datar = desc.replace("Description = '", "")
        x = datar.rstrip("'")
        bb = line.split('plugins/Payloads/')[1].split('.plugin')[0]
        if x == "#!/usr/bin/python":
            x = "\033[1;91mDescription has not yet been implemented.\033[1;m"
        print " %s\t   %s" % (bb,x)
    print " "

def utilities():
    print ""
    print "Plugin Category: Utilities"
    print "==============================\n"
    print " Name              Description"
    print " ----              -----------"
    directory_list = glob.glob('plugins/Utilities/*.plugin')
    for line in directory_list:
        about = line
        with open(about, 'r') as myfile:
            data = myfile.read().splitlines()
            desc = data[0]
            datar = desc.replace("Description = '", "")
        x = datar.rstrip("'")
        bb = line.split('plugins/Utilities/')[1].split('.plugin')[0]
        if x == "#!/usr/bin/python":
            x = "\033[1;91mDescription has not yet been implemented.\033[1;m"
        print " %s\t   %s" % (bb,x)
    print " "
