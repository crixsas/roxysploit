#!/usr/bin/python

import subprocess
import os

def update():
	print "[*]Updating roxysploit framework, Please Wait ..."
	try:
		subprocess.Popen("rm -rf /opt/roxysploit; cd /opt;git clone https://github.com/Eitenne/roxysploit.git", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
		subprocess.Popen("chmod +x /opt/roxysploit/*", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
		subprocess.Popen("mkdir /opt/roxysploit/storage/logs", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
		subprocess.Popen("cp /opt/roxysploit/storage/config-skeleton.xml /opt/roxysploit/storage/logs/config.xml", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
	except Exception, e:
		print "[!] Update Failed."
		pass

	print "[*]Update was completed successfully."
if __name__ == "__main__":
	update()
