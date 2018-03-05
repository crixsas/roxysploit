#!/usr/bin/python

import os, time, subprocess
from sys import stdout
import sys
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

def Command_exe(msg,cmd):
    	i = "\033[1mSTATUS"+colors.W+":[Processing]"
	stdout.write(" " + msg + " %s" % i)
	stdout.flush()
	if subprocess.call(cmd+' >/dev/null 2>&1', shell=True)==0:
		i = "[\033[1m"+colors.G+"OK"+colors.W+"]"
	else:
		i = "["+colors.R+"\033[1mERROR"+colors.W+"]["+colors.O+"\033[1mWARNING"+colors.W+"]"
		
	stdout.write("\r " + msg +" STATUS:%s" % i)

class banner:
    logo = colors.G + """                                          
                                                         `                                          
                                                  `.:-  +yo`                                        
                                                 .oohs/.hyy-                                        
                                                 omhhssyy++.                                        
                                                 omhyss+o+/                                         
                                                 smdhdy+ss`                                         
                                                 -mdyo++s:                                          
                                        ..: -` `.+mdhsoo:`                                          
                                        .:+:syyyhmmmdyso` `                                         
                                     :::osyhdhhhyyhhdhyy+-:`                                        
                                     -osyyhdyddys/++ohhyyyy/`                                       
                                    /hyhmhhmhhdyo+//+sh+/++y+.                                      
                                   :hhydhhmNmmmhsso/+ydo///shs.                                     
                               `   yhyyhymmmmdddhhsoohmyso+sdy/                                     
                              `:`.shyhyo.smmddydhdddddddhyydyhs.                                    
                               :+hmyys-   ommdhydmdhysydydyddsy+                                    
                               /hddsy`     ymdddddhdsoydhh+/mdys:                                   
                               hyhdy/      `+mmmhhddyssssh: /ddds:`                                 
                               dshys.        ydmdydhso++so` `hddhso`                                
                              `myss-         /mmmdhhsssyyo   .ohhhs+                                
                              :mys:          sddhdhdhhsoss`    /hhdy-                               
                              /mss          .dydddhdysooyy+     .shho                               
                              ymy/           yhhdmdhyyyhdhy.      +hd:                              
                              dmdo          +mdhdhdhssyhhhyo`      shs`                             
                             .mmds.        `mhddddyyhdhsyhyy`    `+hhy-                             
                             /mmdhy`       :dhhmddyshddhyhhs`    :dyhs.                             
                              :yddo        .dhhhmdshhhmdyhys.     +/+-                              
                               `o-         `mdhohdshymmmhyyh/                                       
                                           smmyoohdyhNmmhhos/                                       
                                           hddmsoyyhdNdmddos:                                       
                                          .dmymhssho+mmdhdy+.                                       
                                         `ydmsmhyho.`dmddhhs`                                       
                                         odmdsmddy:  ommhhhs-                                       
                                         ddmyhddhs.  .dmddhs.                                       
                                        /mddydhyy`   .mNddd+                                        
                                       :dmmhhdyy.    hmmdhy:                                        
                                      /hmmdddhho    -mmmdhs:                                        
                                      /mddmhhhh-    hmmddho`                                        
                                      +mmmhddds    `mdmmhh:                                         
                                      hmmddmmh/    `dmmmds`                                         
                                     `dmddmddy.     ymmdd:                                          
                                     .mmdmmdh/     .hmmdh-                                          
                                    `oymddddh/     /dmmdhs-                                         
                                     ++mdddhh/    `ymmmdhhh:`                                       
                                     oymdddhh.    -mdmmdhdhyso:``                                   
                                    /mmddddh+    -ymmdmmhyhhyyso+-                                  
                                   -dmmdmddhs-  `-:oyoooohshys.                                     
                                   ommdhmdhdhs-          :-                                         
                                  -hdmddmdhydyy+`             ``                                    
                                .+ysydhdddyhdyo/-.         .::::--`                                 
                                    .++-ohsy::::-         .-:`````                                  
                                        ..."""

print banner.logo

if os.getuid() != 0:
    	print " ["+colors.R+"-"+colors.W+"] ERROR:"+colors.B+" Install"+colors.B+" must be run as "+colors.R+"root"+colors.W+"."
	print " ["+colors.R+"-"+colors.W+"] login as root ("+colors.R+"sudo"+colors.W+") or try "+colors.W+"sudo python installer.py"+colors.W+"\n"
	exit(1)

time.sleep(1)
print Command_exe("["+time.strftime('%H:%M:%S')+"] Making python2 as default.                 ",'mv /usr/bin/python2 /usr/bin/python')
print Command_exe("["+time.strftime('%H:%M:%S')+"] Fixing python3.                 ",'mv /usr/bin/python3 /usr/bin/python3')

print Command_exe("["+time.strftime('%H:%M:%S')+"] Moving console startup into directory.                 ",'mv rsfc /usr/bin/rsfc')
print Command_exe("["+time.strftime('%H:%M:%S')+"] Giving permision to access console.                 ",'chmod +x /usr/bin/rsfc')
print Command_exe("["+time.strftime('%H:%M:%S')+"] Moving updater into the directory.                 ",'mv rsfupdate /usr/bin/rsfupdate')
print Command_exe("["+time.strftime('%H:%M:%S')+"] Giving permision to the updater.                 ",'chmod +x /usr/bin/rsfupdate')

print Command_exe("["+time.strftime('%H:%M:%S')+"] Creating a main directory.                 ",'mkdir /opt/roxysploit')
print Command_exe("["+time.strftime('%H:%M:%S')+"] Moving contents into main directory.                 ",'cp -r * /opt/roxysploit/')
print Command_exe("["+time.strftime('%H:%M:%S')+"] Creating log file directory.                 ",'mkdir /opt/roxysploit/storage/logs')

print """\n
1. ArchLinux
2. Debian/Ubuntu/Kali
3. Fedora
"""
options = raw_input("os > ")
if options == "1":
    print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing pip.                 ",'pacman -S python2-pip')
    print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing wine and winetricks.                 ",'pacman -S wine winetricks')
    print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing android-tools-adb.                 ",'pacman -S android-tools-adb')
    print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing android-tools-adb.                 ",'pacman -S android-tools-fastboot')
elif options == "2":
    print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing pip.                 ",'apt-get -y install python2-pip')
    print Command_exe("["+time.strftime('%H:%M:%S')+"] Getting wine architecture.                 ",'dpkg --add-architecture i386')
    print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing wine and winetricks.                 ",'apt-get -y install wine32 winetricks')
    print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing android-tools-adb and android-tools-fastboot.                 ",'apt-get -y install android-tools-adb android-tools-fastboot')
elif options == "3":
    print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing pip.                 ",'dnf install python2-pip')
    print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing wine and winetricks.                 ",'dnf install wine32 winetricks')
    print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing android-tools-adb and android-tools-fastboot.                 ",'dnf install android-tools-adb android-tools-fastboot')
else:
    sys.exit()
print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing logging.                 ",'python2 -m pip install logging')
print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing impacket.                 ",'python2 -m pip install impacket')
print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing pysmb.                 ",'python2 -m pip install pysmb')
print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing pycrypto.                 ",'python2 -m pip install pycrypto')
print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing paramiko.                 ",'python2 -m pip install paramiko')
print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing scapy.                 ",'python2 -m pip install scapy')
print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing whois.                 ",'python2 -m pip install whois')
print Command_exe("["+time.strftime('%H:%M:%S')+"] Installing terminaltables.                 ",'python2 -m pip install terminaltables')

print "["+time.strftime('%H:%M:%S')+"] run '" + colors.G + "rsfc'"
