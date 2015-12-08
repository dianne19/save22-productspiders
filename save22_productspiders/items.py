# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Save22ProductspidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    sku = scrapy.Field()
    ean = scrapy.Field()
    mfr = scrapy.Field()
    brand = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    image_urls = scrapy.Field()
    currency = scrappy.Field()
    price = scrappy.Field()
    old_price = scrappy.Field()
    offer = scrappy.Field()
    stock = scrappy.Field()
    
    #pass
    
