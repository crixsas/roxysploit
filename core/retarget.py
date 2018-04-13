#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time
from lxml import etree

def edit():
    time.sleep(0.1)
    XML = "storage/logs/config.xml"
    CHECK_XML = os.path.exists(XML)

    if CHECK_XML == False:
       os.system('cp storage/config-skeleton.xml storage/logs/config.xml')
    else:
       var = "1"

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
    print "\033[1;92m[+]\033[1;m Completed."
