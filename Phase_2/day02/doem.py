import requests as ret
def get_data(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    da=ret.get(url,headers=header)
    da.encoding='gbk'
    return da.text

def extract_data(data):
    hero_list=[]
    return hero_list

def save_data():
    pass

if __name__ == '__main__':
    url = 'https://pvp.qq.com/web201605/herolist.shtml'
    data=get_data(url)
    with open('./wzry.html','w',encoding='utf-8') as op:
        op.write(data)
        op.flush()