import requests
import scrapy


class RenrencheSpider(scrapy.Spider):
    name = "renrenche"
    allowed_domains = ["www.renrenche.com"]
    start_urls = ["https://www.renrenche.com/fs/ershouche/?plog_id=44119d506369fdc6bf4207d9771541c4"]

    def parse(self, response):
        carlist_href=response.xpath("//div[@class='brand-more-content']/div/p/span[@class='bn']/a/@href")
        print(carlist_href,"d"*40)
        for carhref in carlist_href:
            carhref="https://www.renrenche.com"+carhref

            print(carhref)
            yield requests.Request(url=carhref,backcall=self.car_parse)


    def car_parse(self,response):
        pass