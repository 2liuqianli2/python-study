# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HelloScrapyPipeline:
    def process_item(self, item, spider):
        return item

class QuotePipeline:

    def process_item(self, item, spider):
        with open('./Quote.txt', "a", encoding='utf-8') as op:
            op.write(item.get("content"))
            op.flush()

        return item