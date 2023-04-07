import requests


def chat_robot(url,mess):
    res=requests.get(url+mess,headers={"user_agent":"python robot"})
    return res.json()["content"]




if __name__ == '__main__':
    name=input("请设置你的名字:")
    url="http://api.qingyunke.com/api.php?key=free&appid=0&msg="
    while True:

        mess=input(name+":")
        a=chat_robot(url,mess)
        print("robot:"+a)