#!/usr/bin/env python
#-*-coding:utf-8-*-

import os
import time
import urllib2 
import sys


# https://github.com/racaljk/hosts
hosts_url = "https://raw.githubusercontent.com/racaljk/hosts/master/hosts"

systemroot = os.environ.get('SYSTEMROOT')
host_file = os.path.join(systemroot,'system32\drivers\etc\hosts')
host_file_bak = host_file + "_" + str(int(time.time()))+".bak"

def usage():
	  print "Usage:"
	  print "%s update" %sys.argv[0].split('\\')[-1]
	  print "%s flush" %sys.argv[0].split('\\')[-1]
	  
def down_host():
    host_data = urllib2.urlopen(hosts_url).read()
    with open(host_file,'w')as f:
        f.write(host_data)
    print "Hosts update successfully !"
    
def backup_host():
    try:
        os.rename(host_file, host_file_bak)
        return True
    except Exception:
        print "Hosts update failed !"
        print "Check %s" %(os.path.join(systemroot,'system32\drivers\etc'))
        #print Exception
        return False
        
def update_host():
    if backup_host():
        down_host()
                 
def flush_host():
    if backup_host():
        with open(host_file,'w')as f:
        	   f.write('')
        print "Host flush successfully !"

def main():
    if(len(sys.argv) == 2):
    	  if(sys.argv[1] == 'update'):
    	      update_host()
    	  if(sys.argv[1] == 'flush'):
            flush_host()
    else:
    	  usage()
        

if __name__ == "__main__":
    main()