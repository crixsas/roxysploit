#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys
import string
import time
import random
import sys
import os
import glob
from lxml import etree
from urlparse import urlparse
from struct import pack
import rlcompleter, readline
import subprocess
from sys import stdout
from subprocess import check_output

class colors:
    W  = '\033[0m'  
    R  = '\033[31m' 
    G  = '\033[32m' 
    O  = '\033[33m' 
    B  = '\033[34m' 
    P  = '\033[35m' 
    C  = '\033[36m' 
    GR = '\033[40m'
    GY = '\033[43m'
    GE = '\033[41m'
    GW = '\033[4m'
    HH = '\033[1m'

intname = "rsf"
det = sys.argv[0]
dala = det.split('.')[-2]
fin = dala.split('plugins/')[-1]
__plugin__      = "%s.plugin" % (fin)
RescoursesDir = os.getcwd()
dandtime = time.strftime("%H:%M:%S")

tabcomp = ['help','execute','info','exit']

def completer(text, state):
    options = [x for x in tabcomp if x.startswith(text)]
    try:
        return options[state]
    except IndexError:
        return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

def dashboard():
    try:
        line_1 = "" + intname + "(\033[1;31m" + fin + "\033[1;m) > "
        terminal = raw_input(line_1).lower()
        time.sleep(0.2)
        if terminal == 'help':
            print "Core Commands"
            print "============="
            print ""
            print "  Command         Description"
            print "  -------         -----------"
            print "  help            show help menu"
            print "  execute         run the plugin"
            print "  exit            exit the current plugin"
            print "  info            show plugin description"
            print ""
            dashboard()
        elif terminal == 'execute':
            pass
        elif terminal == "info":
            with open("plugins/" + fin + ".plugin", 'r') as myfile:
                data = myfile.read().splitlines()
                desc = data[0]
                datar = desc.replace("Description = '", "")
                x = datar.rstrip("'")
                if x == "#!/usr/bin/python":
                    x = "\033[1;91mDescription has not yet been implemented.\033[1;m"
                print x
            dashboard()
        elif terminal == 'exit':
            sys.exit()
        else:
            print "Unknown syntax: %s" % (terminal)
            dashboard()
    except KeyboardInterrupt:
        sys.exit()

class ask():
    tree = etree.parse("Recoureses/lhost.xml")
    for l in tree.xpath("/configuration/config/default_target"):
        lhost = "%s" % (l.text)

    treebunck = etree.parse("storage/logs/config.xml")
    for t in treebunck.xpath("/configuration/config/default_target"):
	    target = "%s" % (t.text)

    buckit = etree.parse("Recoureses/lport.xml")
    for f in buckit.xpath("/configuration/config/default_target"):
	    lport = "%s" % (f.text)

    shitlist = etree.parse("Recoureses/mac.xml")
    for z in shitlist.xpath("/configuration/config/default_target"):
	    mac = "%s" % (z.text)

def run(cmd):
    x = check_output(cmd, shell=True)
    i = "[\033[1m"+colors.B+"!"+colors.W+"] "
    print i + x

def warning(msg):
    print "[\033[1m"+colors.O+"/"+colors.W+"]", msg

def fail(msg):
    print "[\033[1m"+colors.R+"?"+colors.W+"]", msg

def success(msg):
    print "[\033[1m"+colors.G+"!"+colors.W+"]", msg

def text(msg):
    print "\033[1;94m[*]\033[1;m", msg
