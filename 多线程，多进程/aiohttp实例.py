import time
import asyncio
import aiohttp
import os
import requests
from lxml import etree
import re

path="./多线程，多进程/aiohttp实例视频/" 
if not os.path.exists(path):
    os.mkdir(path)

start_time=time.time()

headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }

# urls=[
#     "https://video.pearvideo.com/mp4/third/20191120/cont-1624716-10964589-180710-hd.mp4",
#     "https://video.pearvideo.com/mp4/adshort/20191120/cont-1624622-14612668_adpkg-ad_hd.mp4",
#     "https://video.pearvideo.com/mp4/third/20191121/cont-1624965-11472701-151804-hd.mp4"
#     ]
def find_url(url):     #遍历抓取视频url的函数
    res=requests.get(url=url,headers=headers).text
    tree=etree.HTML(res)
    name=tree.xpath('//div[@class="popularem-ath"]/a/h2/text()')
    detail_url=tree.xpath('//li[@class="popularem clearfix"]/div[@class="popularem-ath"]/a/@href')
    video_lis=[]
    for n,d in zip(name,detail_url):
        video_name=n+".mp4"
        video_path=path+video_name
        detail_url="https://www.pearvideo.com/"+d
        res_detail=requests.get(url=detail_url,headers=headers).text
        video_url=re.findall(r'srcUrl="(.*?)",vdoUrl=',res_detail)[0]
        video_lis.append(video_url)
    return video_lis

async def get_page(url):  
    async with aiohttp.ClientSession() as session:   #所有with前必须有async修饰
        async with await session.get(url,headers=headers) as res:  #耗时的操作必须进行挂起操作
            down_time=time.time()
            page_text=await res.read()  #在获取响应数据之前必须手动挂起
            name=url.split("/")[-1]
            path_name=path+name
            with open(path_name,"wb") as f:
                f.write(page_text)
            print(url+" 下载完成,用时: %.2f秒"%(time.time()-down_time))

urls=find_url("https://www.pearvideo.com/popular_4")
tasks=[]
for url in urls:
    c=get_page(url)
    task=asyncio.ensure_future(c)
    tasks.append(task)

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print(time.time()-start_time)