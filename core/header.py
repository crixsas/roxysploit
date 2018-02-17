#!/usr/bin/env python
import os
import random

def main_header():
	ban = random.choice(os.listdir("banners"))
	banextenstion = "banners/%s" % (ban)
	ban_open = open(banextenstion, "r")
	print ban_open.read()
	ban_open.close()
