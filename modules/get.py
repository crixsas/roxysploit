#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys
import string
import time
import random
import sys
import os
from lxml import etree
from urlparse import urlparse
from struct import pack

intname = "rsf"
det = sys.argv[0]
dala = det.split('.')[-2]
fin = dala.split('plugins/')[-1]
__plugin__      = "%s.plugin" % (fin)
RescoursesDir = os.getcwd()
dandtime = time.strftime("%H:%M:%S")


#tree = etree.parse("storage/logs/config.xml")
#for user in tree.xpath("/configuration/config/default_target"):
#	ip = "%s" % (user.text)

def lhost():
    tree = etree.parse("Recoureses/lhost.xml")
    for user in tree.xpath("/configuration/config/default_target"):
        print "\033[1;94m[?]\033[1;m Listener :: Enter a listening host"
        default_target = raw_input('\033[1;92m[+]\033[1;m Listener [' + user.text + ']: ') or user.text
    retarget_xml = """<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <config name="roxysploit">
      		<default_target>""" + default_target + """</default_target>
    </config>
</configuration>"""
    retarget_file = open("Recoureses/lhost.xml", "w")
    retarget_file.write(retarget_xml)
    retarget_file.close()


def target():
    tree = etree.parse("storage/logs/config.xml")
    for user in tree.xpath("/configuration/config/default_target"):
        print "\033[1;94m[?]\033[1;m Target :: Enter a targets address"
        default_target = raw_input('\033[1;92m[+]\033[1;m Target [' + user.text + ']: ') or user.text
    retarget_xml = """<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <config name="roxysploit">
      		<default_target>""" + default_target + """</default_target>
    </config>
</configuration>"""
    retarget_file = open("storage/logs/config.xml", "w")
    retarget_file.write(retarget_xml)
    retarget_file.close()


def lport():
    tree = etree.parse("Recoureses/lport.xml")
    for user in tree.xpath("/configuration/config/default_target"):
        print "\033[1;94m[?]\033[1;m Lport :: Enter a listening port"
        default_target = raw_input('\033[1;92m[+]\033[1;m Lport [' + user.text + ']: ') or user.text
    retarget_xml = """<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <config name="roxysploit">
      		<default_target>""" + default_target + """</default_target>
    </config>
</configuration>"""
    retarget_file = open("Recoureses/lport.xml", "w")
    retarget_file.write(retarget_xml)
    retarget_file.close()


def mac():
    tree = etree.parse("Recoureses/mac.xml")
    for user in tree.xpath("/configuration/config/default_target"):
        print "\033[1;94m[?]\033[1;m Mac :: Enter a mac address"
        default_target = raw_input('\033[1;92m[+]\033[1;m MAC [' + user.text + ']: ') or user.text
    retarget_xml = """<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <config name="roxysploit">
      		<default_target>""" + default_target + """</default_target>
    </config>
</configuration>"""
    retarget_file = open("Recoureses/mac.xml", "w")
    retarget_file.write(retarget_xml)
    retarget_file.close()
