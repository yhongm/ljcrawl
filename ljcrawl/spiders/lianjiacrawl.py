# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
import time
import re
from ljcrawl.items import LjcrawlItem


class LianjiacrawlSpider(scrapy.Spider):
    name = "lianjiacrawl"
    allowed_domains = ["bj.lianjia.com","bj.zu.ke.com"]
    # start_urls = ['http://bj.lianjia.com/'] #lianjia
    start_urls = ['https://bj.zu.ke.com'] #beike

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
        house_lit_li = sel.css('.content__list .content__list--item')
        print("page:"+str(page)+",length:"+str(len(house_lit_li)))
        for li in  house_lit_li:
            
             house_name = re.sub(r'\s+','',li.xpath('./div[@class="content__list--item--main"]/p[@class="content__list--item--title twoline"]/a/text()').extract_first())
            #  print("house_name:"+house_name)
            # #  
             house_price=li.xpath('./div[@class="content__list--item--main"]/span[@class="content__list--item-price"]/em/text()').extract_first()
            #  print("house_price:"+house_price)
             where_sel=li.xpath('./div[@class="content__list--item--main"]/p[@class="content__list--item--des"]')
             xiaoqu=where_sel.xpath('./a[3]/text()').extract_first()
            #  print("xiaoqu:"+xiaoqu)
             zone=re.sub(r'\s+','',where_sel.xpath('./text()[7]').extract_first())
            #  print("zone:"+zone)
             meters=re.sub(r'\s+','',where_sel.xpath('./text()[5]').extract_first())
            #  print("meters:"+meters)
             directon=where_sel.xpath('./text()[6]').extract_first()
            #  print("directon:"+directon)
            #  con_sel=li.xpath('*[@class="info-panel"]/div[@class="col-1"]/div[@class="other"]/div[@class="con"]')
             region=where_sel.xpath('./a[2]/text()').extract_first()
            #  print("region:"+region)
             
             floor=re.sub(r'\s+','', where_sel.xpath('./span[@class="hide"]/text()').extract()[1])
            #  print("floor:"+floor)
             area=where_sel.xpath('./a[1]/text()').extract_first()
            #  print("area:"+area)
             item= LjcrawlItem()
             item['house_name'] = house_name
             item['house_price'] = house_price
             item['area'] = area
             item['region'] = region
             item['xiaoqu'] = xiaoqu
             item['zone'] = zone
             item['meters'] = meters
             item['directon'] = directon
             item['floor'] = floor
             
             yield item
