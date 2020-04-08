import requests
from lxml import etree
import re
import os
import time
from multiprocessing.dummy import Pool



headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }

url="https://video.pearvideo.com/mp4/third/20191121/cont-1624942-13182825-143409-hd.mp4"
video_data=requests.get(url=url,headers=headers).content
print(video_data)