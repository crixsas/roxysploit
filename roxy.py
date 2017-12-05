#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time
import readline, rlcompleter
import os.path
from time import sleep
from core import menu
from core import modules
from core import help
from core import header
import platform
from plugins import *
import rlcompleter, readline
import os.path
import logging
import re
import glob
from terminaltables import DoubleTable
from os.path import join
from core import pluginfinder
from subprocess import check_output
from lxml import etree
os.system('clear')

time.sleep(1)
if not os.geteuid() == 0:
    sys.exit("""\033[1;91m\n[\033[1;m!\033[1;91m]\033[1;m RoxySploit Requires root access!!\n\033[1;m""")


version = "4.8.0"
intname = "rsf"
lan_ip = os.popen("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'").read()
public_ip = os.popen("wget http://ipinfo.io/ip -qO -").read()

dir = "plugins/"
test=os.listdir(dir)

for item in test:
    if item.endswith(".plugin"):
        plugins_all = item.split('.')[0]

options_sl = ['clean','others','gen','all','plugin','?','clear','exit','banner','help', 'show','ipnet','exploits','payloads','utilities']
addrs = glob.glob("plugins/*.plugin")
total_plugins = len(addrs)
tabcomp = options_sl
tabcomp +=addrs

def completer(text, state):
    options = [x for x in tabcomp if x.startswith(text)]
    try:
        return options[state]
    except IndexError:
        return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

RescoursesDir = os.getcwd()

LOGS = "storage/logs"
PLUGINS = "plugins"
STORAGE = "storage"
MODULES = "modules"
CORE = "core"
CHECK_LOGS = os.path.exists(LOGS)
CHECK_STORAGE = os.path.exists(STORAGE)
CHECK_MODULES = os.path.exists(MODULES)
CHECK_CORE = os.path.exists(CORE)
CHECK_PLUGINS = os.path.exists(PLUGINS)

if CHECK_PLUGINS == False:
    print "Missing files..."
    sys.exit()
else:
    var = "1"

if CHECK_CORE == False:
    print "Missing files..."
    sys.exit()
else:
    var = "1"

if CHECK_MODULES == False:
    print "Missing files..."
    sys.exit()
else:
    var = "1"

if CHECK_STORAGE == False:
    print "Missing files..."
    sys.exit()
else:
    var = "1"

os.system('clear')
time.sleep(0.1)
print "\033[1;94m[?]\033[1;m Starting Roxy Exploitation Framework..."
time.sleep(20)
RescoursesDir = os.getcwd()

dandtime = time.strftime("%d-%m-%Y-%H:%M:%S")

logfile = "%s/storage/logs/%s.log" % (RescoursesDir,dandtime)

if CHECK_LOGS == True:
    filename_logging = os.path.join(os.path.dirname(__file__), logfile)
    logging.basicConfig(filename=filename_logging, filemode='w', level=logging.DEBUG)
    print "\033[1;94m[?]\033[1;m Creating logfile:", logfile
else:
    print "\033[1;31m[?]\033[1;m Failed Creating logfile:", logfile

time.sleep(1)

XML = "storage/logs/config.xml"
CHECK_XML = os.path.exists(XML)

if CHECK_XML == False:
    os.system('cp storage/config-skeleton.xml storage/logs/config.xml')
else:
    var = "1"

print "\033[1;94m[*]\033[1;m Retargetting Session"
time.sleep(1)
tree = etree.parse("storage/logs/config.xml")
for user in tree.xpath("/configuration/config/default_target"):
	default_target = raw_input('\033[1;92m[+]\033[1;m Default Target IP Address [' + user.text + ']: ') or user.text

retarget_xml = """<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <config name="roxysploit">
      		<default_target>""" + default_target + """</default_target>
    </config>
</configuration>"""

retarget_file = open("storage/logs/config.xml", "w")
retarget_file.write(retarget_xml)
retarget_file.close()

print "\033[1;94m[?]\033[1;m Initializing Global State"
time.sleep(0.9)
print "\033[1;92m[+]\033[1;m Set TargetIp => %s" % (default_target)
time.sleep(2)
print "\033[1;92m[+]\033[1;m Loaded plugins => %s" % (total_plugins)
time.sleep(0.3)
print "\033[1;92m[+]\033[1;m Detected Version => %s" % (version)
time.sleep(1)
header.main_header()
print """
::\033[1;33mRoxy Exploitation Framework\033[1;97m
::Codename : https://github.com/Eitenne
"""

def main():
    try:
        line_1 = "\033[1;4m" + intname + "\033[1;24m > "
        terminal = raw_input(line_1).lower()
        logging.info(terminal)
        time.sleep(0.5)
        if terminal[0:3] =='use':
            if terminal[4:] == terminal[4:]:
                os.system('python plugins/%s.plugin' % (terminal[4:]))
                main()
            #elif terminal[4:32] =='example':
                #example()
                #main()
        if terminal[0:6] == 'search':
            print "\033[1;94m[?]\033[1;m Searching %s" % (terminal[7:])
            time.sleep(1)
            names = addrs
            found = []
            for name in names:
                if terminal[7:] in name:
                    found.append(name)
            print found
            main()
        elif terminal[0:13] == 'show payloads':
            modules.payloads()
            main()
        elif terminal[0:14] == 'show exploits':
            modules.exploits()
            main()
        elif terminal[0:94] == 'show utilities':
            modules.utilities()
            main()
        elif terminal[0:15] == 'show others':
            modules.others()
            main()
        elif terminal[0:17] == 'show all':
            modules.all()
            main()
        elif terminal[0:4] =='help':
            help.help()
            main()
        elif terminal[0:41] =='plugin':
            os.system('python plugins/hello.plugin')
            main()
        elif terminal[0:7] == 'show':
            showlist()
            main()
        elif terminal[0:2] =='?':
            help.help()
            main()
        elif terminal[0:5] =='ipnet':
            os.system('wine cmd.exe /c ipconfig')
            main()
        elif terminal[0:8] =='clean':
            os.system("echo 'Cleaning evidence ;)'; rm storage/logs/*")
            main()
        elif terminal[0:5] =='clear':
            os.system('clear')
            main()
        elif terminal[0:6] =='banner':
            os.system('clear')
            postit()
 	    menu.main_info()
            main()
        elif terminal[0:9] =='exit':
            exit()
        elif terminal[0:1] =='!':
            os.system(terminal[1:])
            main()
        else:
            print "Command not found:", terminal
            main()
    except(KeyboardInterrupt):
        print "\n"
        return main()

def showlist():
	print """
Plugin Category
===============

 Name
 ----
 Payloads
 Exploits
 Utilities
 Others
 All
"""

def postit():
	header.main_header()
	print """
::\033[1;33mRoxy Exploitation Framework\033[1;97m
::Codename : https://github.com/Eitenne
	"""


def start():
    menu.main_info()
    main()

if __name__=='__main__':
    start()
