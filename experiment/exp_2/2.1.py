import re

class finds1122():
    def __init__(self, *args):
        self.pattern=args[0]
        self.string=args[1]


    def func(self):
        data=re.findall(pattern=self.pattern,string=self.string)
        return data




if __name__ == '__main__':
    pattern=re.compile('<span>(.*?)</span>',re.S)
    string = '<span>无敌爬虫，越用越爽</span>,<span>嘻嘻哈哈</span>'

    re_object=finds1122(pattern,string)
    text=re_object.func()
    print(text)
