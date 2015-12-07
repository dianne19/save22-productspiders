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
        Rule(LinkExtractor(allow=(r'.+sg/\S+\d+/', ), deny=(r'.+/.filter', ))),
        Rule(LinkExtractor(allow=(r'.+sg/?page.+', )), deny=(r'.+/.filter', )),
    )
    

    def parse_item(self, response):
        for href in response.css("div#product_listing > div.productGrid > ul.item.c0 > li.image > a::attr('href')"):
          url = response.urljoin(href.extract())
          request = scrapy.Request(url, callback=self.parse_dir_contents)
          yield request      

    def parse_dir_contents(self, response): 
      items = list()

          for sel in response.xpath('//*[@id="prod_core"]'):
            item = Save22ProductspidersItem()
            
              item['Link'] = response.url or None
              item['Title'] = sel.xpath('@data-name').extract()
              item['Description'] = sel.xpath('@data-desc').extract()
              item['Image_Link'] = sel.xpath('@data-imgurl').extract()
          #    item['Quality'] = sel.xpath('@data-selqty').extract()
              item['Price'] = sel.xpath('@data-price').extract()
              item['Old_price'] = sel.xpath('@data-oldprice').extract()
              item['Offer'] = sel.xpath('@data-outofstock').extract()
              items.append(item)
              yield item
             return