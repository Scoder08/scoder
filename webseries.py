import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
from bs4 import BeautifulSoup as bs
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
web=input("Web series name : ")
season=int(input("Season : "))
episode=int(input("Episode : "))
# to search 
url="http://dl.sitemovie.ir/serial/"
a=urllib.request.urlopen(url,context=ctx).read()
soup=bs(a,'html.parser')
L=soup.find_all('a')
counts=0
for i in L:
	if i.text[:len(i.text)-1].lower()==web.lower():
		url+=i.get('href')
		a=urllib.request.urlopen(url,context=ctx).read()
		soups=bs(a,'html.parser')
		L1=soups.find_all("a")
		try:
			count=0
			for j in L1:
				a=re.findall('([0-9]+)/',j.text)
				if len(a)>0:
					if int(a[0])==season:
						url+=j.get('href')
						break
			a=urllib.request.urlopen(url,context=ctx).read()
			soupe=bs(a,'html.parser')
			Le=soupe.find_all('a')
			count=1
			for k in Le:
				b=re.findall('E([0-9]+)_',k.text)
				if len(b)>0:
					if int(b[0])==episode:
						url+=k.get("href")
						break
			print(url)
			print("-------Downloading-------")
			urllib.request.urlretrieve(url, web+"S"+str(season)+"E"+str(episode)+".mkv")
			print("\n			 downloading completed ..............") 
		except:
			if count==0:
				print("Try other season. this season not available")
			else:
				print("Try other episode. this episode not available")
		break
	else:
		counts+=1
		continue
x=""
if counts==len(L):
	for i in range(1,len(L)):
		x+=L[i].text[:-1]+"\n"
	print("\n\nI am sorry i don't have this web series, here is a list of webseries\n\n")
	print(x)
