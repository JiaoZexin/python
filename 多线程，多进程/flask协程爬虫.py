# import asyncio
# import requests
# import aiohttp
# import time

# start_time=time.time()
# urls=[
#     "http://127.0.0.1:5000/tian","http://127.0.0.1:5000/jian","http://127.0.0.1:5000/ying"
# ]
# async def get_page(url):
#     print("正在下载",url)
#     res=requests.get(url=url)  #requests模块是同步的,必须使用异步的网络请求模块
#     print("下载完毕",res.text)
# tasks=[]

# for url in urls:
#     c=get_page(url)
#     task=asyncio.ensure_future(c)
#     tasks.append(task)

# loop=asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))

# print(time.time()-start_time)

import asyncio
import requests
import aiohttp
import time

start_time=time.time()
urls=[
    "http://127.0.0.1:5000/tian","http://127.0.0.1:5000/jian","http://127.0.0.1:5000/ying"
]
async def get_page(url):  
    async with aiohttp.ClientSession() as session:   #所有with前必须有async修饰
        #get()/post  params/data  headers  proxy="http://ip:port"
        async with await session.get(url) as res:  #耗时的操作必须进行挂起操作
            page_text=await res.text()  #在获取响应数据之前必须手动挂起
            #text()字符串格式数据
            #read()二进制格式响应数据
            #json()返回json对象
            print(page_text)

tasks=[]  #创建任务列表

for url in urls:  #将函数的返回值逐一加入列表中
    c=get_page(url)
    task=asyncio.ensure_future(c)
    tasks.append(task)

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))  #将参数传入并运行

print(time.time()-start_time)