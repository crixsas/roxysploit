# python
import os.path
import dns.resolver
import dns.exception
from time import sleep
import argparse
from colorama import init, Fore
import os, sys
import time

print "[*] Starting DNS Bruteforce attack..."
time.sleep(1)
dictfile = sys.argv[2]
wait = 0.06

resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8', '8.8.4.4', '208.67.222.222', '208.67.220.220']


domain = sys.argv[1]

if os.path.exists(dictfile):
    f = open(dictfile, "r")
    for line in iter(f):
        l = line.strip('\n')
        try:
            answer = resolver.query(l + "." + domain)
            ip = ''
            for a in answer:
                ip = ip + str(a) + ' '
            print "\033[1;m[%s]\033[1;97m[FOUND:HOST] \033[1;92m%s.%s %s\033[1;m" % (time.strftime("%H:%M:%S"),l,domain,ip)
        except dns.exception.DNSException as e:
            if isinstance(e, dns.resolver.NXDOMAIN):
                continue
            elif isinstance(e, dns.resolver.Timeout):
                print Fore.RED + 'Time-out'
            else:
                print Fore.RED + 'Unhandled exception'
        finally:
            time.sleep(wait)
    f.close()

