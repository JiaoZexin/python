#coding=utf-8
import requests
import json

def hua2(use_id):
    hua2_url="http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById"
    params={
        "id": use_id
    }

    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }

    res=requests.post(url=hua2_url,params=params,headers=headers)
    return res.json()
re=hua2("270b93b832a54210aa97d2444433bd72")
print(re)