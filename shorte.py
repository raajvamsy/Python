import requests
import time
from selenium import webdriver
from selenium.webdriver.common.proxy import *

i=0
p = raw_input("Enter file location of proxy host list with port 80")
host = [line.rstrip('\n') for line in open(p)]
url = raw_input("Enter the url of shorte site")

while 1>0:
 while(i<len(host)):
   profile = webdriver.FirefoxProfile()
   profile.set_preference("network.proxy.type", 1)
   profile.set_preference("network.proxy.http", host[i])
   profile.set_preference("network.proxy.ssl", host[i])
   profile.set_preference("network.proxy.socks", host[i])
   profile.set_preference("network.proxy.ftp", host[i])
   profile.set_preference("network.proxy.http_port", 80)
   profile.set_preference("network.proxy.ssl_port",  80)
   profile.set_preference("network.proxy.ftp_port",  80)
   profile.set_preference("network.proxy.socks_port",  80)
   profile.update_preferences()
   driver = webdriver.Firefox(profile)
   driver.delete_all_cookies()
   print i
   driver.get(url)
   time.sleep(30)
   driver.close()
   i+=1
 i=0


