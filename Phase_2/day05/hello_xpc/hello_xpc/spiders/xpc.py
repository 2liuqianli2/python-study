import scrapy

from ..items import FilemItem


class XpcSpider(scrapy.Spider):
    name = "xpc"
    allowed_domains = ["www.xinpianchang.com"]
    start_urls = ["https://www.xinpianchang.com/discover/article-1-0-all-all-0-0-hot?from=navigator"]

    def parse(self, response):
        source=response.xpath("//div[@class='sc-5a9b134c-0 ikELow']")
        print(source[0])
        for i in source:
            a=i.xpath("./div[2]/div/a")
            title=a.xpath("./@title").extract_first()
            href=a.xpath("./@href").extract_first()

            # b = i.xpath("./div[1]/a/div[3]/ul")
            view_nums=i.xpath("./div/a/div/ul[@class='sc-bfe1476e-0 keonqP']/li[1]/span[2]/text()").extract_first()
            play_nums=i.xpath("./div/a/div/ul[@class='sc-bfe1476e-0 keonqP']/li[2]/span[2]/text()").extract_first()

            file=FilemItem()
            file["title"]=title
            file["href"] =href
            file["view_nums"]=view_nums
            file["play_nums"] =play_nums

            yield file
            # print(view_nums,play_nums)
            yield scrapy.Request(url=href,callback=self.parse_detail)

    def parse_detail(self,respone):

        detail_href=respone.xpath("//div[@class='xpcplayer-video-wrap']/video/@src")
        print(detail_href)