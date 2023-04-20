# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ByescrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class GuaziCarItem(scrapy.Item):

    car_title = scrapy.Field()
    car_price = scrapy.Field()
    car_price_source = scrapy.Field()
    car_info = scrapy.Field()
    car_brand = scrapy.Field()


class RenRenCarItem(scrapy.Item):
    car_price = scrapy.Field()
    car_price_source = scrapy.Field()
    car_title = scrapy.Field()
    car_kilometre = scrapy.Field()
    car_timedelta = scrapy.Field()
    car_brand = scrapy.Field()