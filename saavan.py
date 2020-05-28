import gevent.monkey
import requests
from bs4 import BeautifulSoup
from json import JSONDecoder
from pyDes import *
import base64
from urllib.parse import unquote
from sys import platform
import html
import os
import json
import logger
import json
import sys
import ast
import urllib3.request
from traceback import print_exc
import subprocess
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

des_cipher = des(b"38346591", ECB, b"\0\0\0\0\0\0\0\0" , pad=None, padmode=PAD_PKCS5)
base_url = 'http://h.saavncdn.com'
json_decoder = JSONDecoder()
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
}

def fate_proxy():
    resp=requests.get('https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list')
    a=((resp.text).split('\n'))
    p_list=[]
    for i in a:
        try:
            p_list.append(json.loads(i))
        except Exception as e:
            continue
    np_list=[]
    for i in p_list:
        if i['country']=='IN':
            np_list.append(i)
    proxy=[]
    fast_proxy=sorted(np_list,key=lambda k: k['response_time'])
    for p in fast_proxy:
      proxy.append(str(p['host'])+':'+str(p['port']))
    return proxy

def get_songs(query,proxies):
    if not query.startswith('https://www.jiosaavn.com'):
        url = "https://www.jiosaavn.com/search/"+query
        flag="link"
    else:
        url=query
        flag="query"
    songs=[]
    try:
        res = requests.get(url, headers=headers, data=[('bitrate', '320')])
        soup = BeautifulSoup(res.text,"lxml")
        all_song_divs = soup.find_all('div',{"class":"hide song-json"})
        for i in all_song_divs:
            try:
                try:
                    song_info= json.loads(i.text)
                    songs.append(song_info)
                except:
                    esc_text = re.sub(r'.\(\bFrom .*?"\)',"",str(i.text))
                    try:
                        song_info = json_decoder.decode(esc_text)
                        songs.append(song_info)
                    except:
                        try:
                            song_info= json.loads(esc_text)
                            songs.append(song_info)
                        except:
                            print(esc_text)

            except Exception as e:
                print_exc()
                continue
        if len(songs)>0:
            return songs
    except Exception as e:
        for test_proxy in proxies:
            try:
                print("Testing with proxy",test_proxy)
                res = requests.get(url, headers=headers, data=[('bitrate', '320')],proxies={"http": test_proxy, "https": test_proxy},timeout=5)
                soup = BeautifulSoup(res.text,"lxml")
                all_song_divs = soup.find_all('div',{"class":"hide song-json"})
                for i in all_song_divs:
                    try:
                        try:
                            song_info= json.loads(i.text)
                            songs.append(song_info)
                        except:
                            song_info = json_decoder.decode(i.text)
                            songs.append(song_info)
                    except Exception as e:
                        #print_exc()
                        continue
            except Exception as e:
                #print_exc()
                continue
            finally:
                if (len(songs)>0):
                    return songs
    return songs

def decrypt_url(url):
    enc_url = base64.b64decode(url.strip())
    dec_url = des_cipher.decrypt(enc_url,padmode=PAD_PKCS5).decode('utf-8')
    dec_url = base_url + dec_url[10:] + '_320.mp3'
    r = requests.get(dec_url)
    if str(r.status_code)!='200':
        dec_url = dec_url.replace('_320.mp3','.mp3')
    return dec_url

proxies=fate_proxy()
query=input("Song Name : ")
query='https://www.jiosaavn.com/search/'+query
song=get_songs(query,proxies)[0]
url=decrypt_url(song['url'])
import urllib.request
urllib.request.urlretrieve(url, "song.mp3")