import requests


def serch_mail(url,mess):

    header={
        'user-agent':'python robot'
    }
    data={
        "appkey":"1e821c400f6ea3db",
        "type":"auto",
        "number":mess
    }
    res=requests.post(url,data=data,headers=header)
    return  res.json()


if __name__ == '__main__':
    url="https://api.jisuapi.com/express/qurey"

    while True:
        a=input('请输入快递单号:')
        # 请输入快递单号:YT7139355536510

        result=serch_mail(url,a)
        # print(result)
        result_inner=result["result"]
        type_name=result_inner["typename"]
        print(type_name)
        list_info=result_inner["list"]

        for info in list_info:
            print(info["time"])
            print(info["status"])