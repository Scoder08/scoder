import requests 
from bs4 import BeautifulSoup as bs 
import json 
import random 
import os.path 
import urllib.request
insta_url ='https://www.instagram.com'
inta_username = ''.join(context.args)

response = requests.get(f"{insta_url}/{inta_username}/") 

if response.ok: 
	html = response.text 
	bs_html = bs(html, features ="lxml") 
	bs_html = bs_html.text 
	index = bs_html.find('profile_pic_url_hd')+21
	remaining_text = bs_html[index:] 
	remaining_text_index = remaining_text.find('requested_by_viewer')-3
	string_url = remaining_text[:remaining_text_index] 
	X=string_url.split('\\u0026')
	print(X)
	string_url="&".join(X)
	print(string_url, "\n \n downloading..........") 


urllib.request.urlretrieve(string_url, "pic1.jpg")
print("\n			 downloading completed ..............") 
