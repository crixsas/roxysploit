import os, sys
import platform
import getpass
version_open = open("storage/version","r")
version = version_open.read()

from lxml import etree

tree = etree.parse("storage/logs/config.xml")
for user in tree.xpath("/configuration/config/default_target"):
	target = user.text

tree = etree.parse("Resources/lhost.xml")
for l in tree.xpath("/configuration/config/default_target"):
    lhost = "%s" % (l.text)

buckit = etree.parse("Resources/lport.xml")
for f in buckit.xpath("/configuration/config/default_target"):
	lport = "%s" % (f.text)

def show():
    print """
Configuration Settings
======================

  Variable          Value
  --------          -----
  ADDR              %s
  TARGET_ADDR       %s
  HOME              %s
  PLATFORM          %s
  PORT              %s
  USER              %s
  HOSTNAME          %s
  ARCH              %s
  RSF_VERSION       %s""" % (lhost, target, os.getcwd(), platform.system(), lport, getpass.getuser(), platform.uname()[1], platform.machine(), version)

show()
