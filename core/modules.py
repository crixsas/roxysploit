#!/usr/bin/env python

def all():
    xla = open("storage/plugins.loaded", "r")
    con = xla.read()
    print ""
    print "Plugin Category: All"
    print "====================\n"
    print "Name"
    print "----"
    print "%s" % (con)
