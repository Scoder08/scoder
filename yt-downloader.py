#To use this first install needed libraries
#pip install youtube_dl
#pip install google

from __future__ import unicode_literals
from googlesearch import search
import youtube_dl
ydl_opts = {}
b=0
query=input("Search on youtube : ")
for i in search(query,  tld = 'com',  
    	                lang = 'en',  
    	                num = 10,     
    	                start = 0,    
    	                stop = None,  
    	                pause = 2.0,  
    	               ):
    if "youtube" in i:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            b=i

        break
print(b)
try:
    ydl.download([b])
except:
    print("I am sorry i can't download this video.")
