import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
from bs4 import BeautifulSoup as bs
from random import randint

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url=input("Keyword for wallpaper : ")
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = url+" unsplash"
  
for j in search(query, tld="co.in", num=1, stop=4, pause=2):
    if "https://unsplash.com/s/photos" in j: 
        url=j 
a=urllib.request.urlopen(url,context=ctx).read()
soup=bs(a,'html.parser')
L=soup.find_all('a',{'title':"Download photo"})
x=randint(1,5)
count=0
for i in L:
    count+=1
    if count==x:
        alink=i.get('href')
        break
    else:
        continue
urllib.request.urlretrieve(alink, "wal.jpg")
print("--------------------------------------------------Downloaded-----------------------------------------------")