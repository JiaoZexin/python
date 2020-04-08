import requests
from lxml import etree
from bs4 import BeautifulSoup
import json
import re

url="https://music.163.com/song?id=1400256289"
lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(1400256289) + '&lv=1&kv=1&tv=-1'
headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }

r=requests.get(url=lrc_url,headers=headers).text

lyric=json.loads(r)['lrc']['lyric']
lyric_r=re.sub(r'\[.*\]','',lyric)
with open("./数据解析1107/lrc.txt","w",encoding="utf-8") as f:
    f.write(lyric_r)
print(lyric_r)



