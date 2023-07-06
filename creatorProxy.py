import requests
import re
from bs4 import BeautifulSoup
import urllib.request
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class creatorProxy:
    url=[]
    def GetSites(self):
        with open("document/sitesProxy.txt",'r') as site:
            self.url=site.readlines()
            site.close()
        self.url = list(map(lambda x: x.strip(), self.url))
        return self.url
    def ParesProxy(self):
        self.GetSites()
        i=0
        for url in self.url:
                try:
                    html=requests.get(url,timeout=(5,10))
                    source=(html.text)
                    proxies = re.findall( r'[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\:[\d]{1,6}', source[5:], re.M|re.I)
                    with open("document/Proxies.txt","a") as file:
                        for prx in proxies:  
                            file.write(prx+'\n')
                        file.close()
                    print(color.BOLD +color.GREEN+ "{} proxies were collected from {}".format(len(proxies),url) + color.END)
                except:
                    print(color.BOLD +color.RED+ "I could not collect from {}".format(url) + color.END)
Proxy=creatorProxy()
Proxy.ParesProxy()
