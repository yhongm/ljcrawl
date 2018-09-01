# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
import time

from ljcrawl.items import LjcrawlItem


class LianjiacrawlSpider(scrapy.Spider):
    name = "lianjiacrawl"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = ['http://bj.lianjia.com/']

    # https: // bj.lianjia.com / zufang / pg1 /

    def start_requests(self):
        for i in range(1, 101):
            request_url = ("%s/zufang/pg%d/" % (self.start_urls[0], i))
            print("ru:" + request_url)
            yield scrapy.Request(url=request_url, meta={"page": i}, callback=self.parse)

    def parse(self, response):
        print("parse:"+str(time.time()))
        page=response.meta["page"]
        sel = Selector(response)
        house_lit_li = sel.css('.house-lst li')
        print("page:"+str(page)+",length:"+str(len(house_lit_li)))
        for li in  house_lit_li:
             house_name = li.xpath('*[@class="info-panel"]/h2/a/text()').extract_first()
             house_price=li.xpath('*[@class="info-panel"]/div[@class="col-3"]/div[@class="price"]/span/text()').extract_first()
             where_sel=li.xpath('*[@class="info-panel"]/div[@class="col-1"]/div[@class="where"]')
             xiaoqu=where_sel.xpath('./a/span[@class="region"]/text()').extract_first()
             zone=where_sel.xpath('./span[@class="zone"]/span/text()').extract_first()
             meters=where_sel.xpath('./span[@class="meters"]/text()').extract_first()
             directon=where_sel.xpath('./span[3]/text()').extract_first()
             con_sel=li.xpath('*[@class="info-panel"]/div[@class="col-1"]/div[@class="other"]/div[@class="con"]')
             region=con_sel.xpath('./a/text()').extract_first()
             floor=con_sel.xpath('./text()').extract()[0]
             description=con_sel.xpath('./text()').extract()[1]
             item= LjcrawlItem()
             item['house_name'] = house_name
             item['house_price'] = house_price
             item['xiaoqu'] = xiaoqu
             item['zone'] = zone
             item['meters'] = meters
             item['directon'] = directon
             item['region'] = region
             item['floor'] = floor
             item['description'] = description
             yield item
