#!/usr/bin/python

import subprocess
import os

def update():
	print "[*]Updating roxysploit framework, Please Wait ..."
	try:
		subprocess.Popen("rm -rf /opt/roxysploit; cd /opt;git clone https://github.com/Eitenne/roxysploit.git", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
	except Exception, e:
		print "[!] Update Failed."
		pass

	print "[*]Update was completed successfully."
if __name__ == "__main__":
	update()
