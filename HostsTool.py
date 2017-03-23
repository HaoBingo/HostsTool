#!/usr/bin/env python
#-*-coding:utf-8-*-

#import requests
import os
import time
import urllib2 


# https://github.com/racaljk/hosts
hosts_url = "https://raw.githubusercontent.com/racaljk/hosts/master/hosts"

systemroot = os.environ.get('SYSTEMROOT')
host_file = os.path.join(systemroot,'system32\drivers\etc\hosts')
host_file_bak = host_file + "_" + str(int(time.time()))+".bak"

def down_host():
    #host_data = requests.get(hosts_url).content
    host_data = urllib2.urlopen(hosts_url).read()
    print host_data
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
    
def main():
    if backup_host():
        down_host()     

if __name__ == "__main__":
    main()
    #down_host()