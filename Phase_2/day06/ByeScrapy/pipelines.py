# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter

from ByeScrapy.items import RenRenCarItem


class ByescrapyPipeline:
    def process_item(self, item, spider):
        return item


class CarPipeline:

    def process_item(self, item, spider):
        # 判定是哪种是 item数据
        if isinstance(item, RenRenCarItem):
            # 创建mysql连接
            con = pymysql.Connect(host="localhost", port=3306, user="rock", password="rock1204", charset="utf8", db="CarData")
            # 获取操作游标
            cursor = con.cursor()
            # 执行插入sql
            cursor.execute("insert into renrencar(car_brand, car_price, car_price_source, car_title, car_timedelta, car_kilometre) VALUES "
                           "('%s', '%s', '%s', '%s', '%s', '%s');" % (item.get("car_brand"), item.get("car_price"), item.get("car_price_source"), item.get("car_title"), item.get("car_timedelta"), item.get("car_kilometre")))
            # 提交操作
            con.commit()
            # 关闭连接
            con.close()

        return item
