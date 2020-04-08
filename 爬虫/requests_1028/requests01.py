import requests
import random

url="http://www.weather.com.cn/weather/101301103.shtml"
header={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
timeout=random.choice(range(80,180))
r=requests.get(url,headers=header,timeout=timeout)
r.encoding="utf-8"
print(r.text)