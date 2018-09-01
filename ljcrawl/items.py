# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LjcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    house_name = scrapy.Field()
    house_price = scrapy.Field()
    xiaoqu = scrapy.Field()
    zone = scrapy.Field()
    meters = scrapy.Field()
    directon = scrapy.Field()

    region = scrapy.Field()
    floor = scrapy.Field()
    description = scrapy.Field()

