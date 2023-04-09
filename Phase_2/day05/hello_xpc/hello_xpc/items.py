# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HelloXpcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class FilemItem(scrapy.Item):
    title=scrapy.Field()
    href=scrapy.Field()
    play_nums=scrapy.Field()
    view_nums=scrapy.Field()