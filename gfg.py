import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
from bs4 import BeautifulSoup as bs

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = ' '.join(context.args)

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = url+" geeksforgeeks"
  
for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
    url=j 
a=urllib.request.urlopen(url,context=ctx).read()
soup=bs(a,'html.parser')
L=soup.find_all('div',{'id':'content'})
print(L[0].text)
L=soup.find_all('div',{'class':'container'})
for i in L:
	print(i.text)
