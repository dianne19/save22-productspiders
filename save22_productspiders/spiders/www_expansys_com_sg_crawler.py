from datetime import datetime
import scrapy

from scrapy.contrib.linkextractors import LinkExtractor 
from scrapy.contrib.spiders import CrawlSpider, Rule
from save22_productspiders.items import Save22ProductspidersItem

class ExpansysItem(CrawlSpider):
    name = "expansys"
    allowed_domains = ["expansys.com.sg"]
    start_urls = [
        "http://www.expansys.com.sg/",
    ]
    
rules = (
        Rule(LinkExtractor(allow=(r'.+sg/\S+\d+/', ), deny=(r'.+/.filter', )), callback = 'parse_item', follow=true),
        Rule(LinkExtractor(allow=(r'.+sg/?page.+', ), deny=(r'.+/.filter', )), callback = 'parse_item', follow=true)
    )
    

def parse_item(self, response):
      items = list()
      sku = list()
      gamit = response.xpath('//*[@id="product"]')
      skui = response.xpath('//@data-sku').extract()

        if skui in sku:
          return
          
          for a in gamit:
              item = Save22ProductspidersItem()
              item['sku'] = skui
              item['Link'] = response.url or None
              item['Title'] = a.xpath('@data-name').extract()
              item['Description'] = a.xpath('@data-desc').extract()
              item['Image_Link'] = a.xpath('@data-imgurl').extract()
              item['Quality'] = a.xpath('@data-selqty').extract()
              item['Price'] = a.xpath('@data-price').extract()
              item['Old_price'] = a.xpath('@data-oldprice').extract()
              item['Offer'] = a.xpath('@data-outofstock').extract()
              items.append(item)
              yield item