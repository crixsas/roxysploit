#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time
from lxml import etree

def edit():
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
    time.sleep(0.9)
    print "\033[1;92m[+]\033[1;m Set TargetIp => %s" % (default_target)
    time.sleep(2)
    print "\033[1;94m[?]\033[1;m ReInitializing Global State"
    time.sleep(1)
    print ""
    print "Name             Set Value"
    print "----             ----------"
    print "TargetIp         %s" % (default_target)
    print "\033[1;92m[+]\033[1;m Configure successful"
