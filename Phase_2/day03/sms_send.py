import hashlib
import random
from time import time

import requests


def send(url,data):
    AppKey="3311503f3cb4285cc574a2f835b5390c"
    Nonce=str(random.random())
    CurTime=str(int(time()))
    hash=hashlib.sha1(("6110861ac8c3"+Nonce+CurTime).encode("utf-8"),)


    CheckSum=hash.hexdigest()
    header={
    "user-agent":"python robot",
    "AppKey":AppKey,
    "Nonce":Nonce,
    "CurTime":CurTime,
    "CheckSum":CheckSum

    }
    res=requests.post(url,data,headers=header)

    return res.json()


if __name__ == '__main__':

    url="https://api.netease.im/sms/sendcode.action"
    a=input("请输入手机号码:")
    data={
        "mobile":a
    }

    text=send(url,data)
    print(text)
