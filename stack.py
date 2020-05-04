import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
from bs4 import BeautifulSoup as bs

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Ask Question : ")

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = url+" stackoverflow"
  
for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
    url=j 
a=urllib.request.urlopen(url,context=ctx).read()
soup=bs(a,'html.parser')
L=soup.find_all('div',{'class':'post-text'})
i=L[0]
print("similar question : "+i.text)
print("================================================")
i=L[1]
print(i.text)
link=i.find_all('a')
for k in link:
	if k:
		print(k.get('href'))
