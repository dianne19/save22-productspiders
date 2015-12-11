import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from save22_productspiders.items import AllforyouItem

class Allporyou(CrawlSpider):
    name = "aporn"
    allowed_domains = ["allforyou.sg"]
    start_urls = [
        "https://allforyou.sg/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow='.+'),
        callback = 'parse_item',
        follow=True)
    ]
    
    def parse(self, response):
        for href in response.css("div.span2.categorybox-span > div.categorybox.thumbnail.text-center > div.thumb > a::attr('href')"):   
          url = response.urljoin(href.extract())
          request = scrapy.Request(url, callback=self.parse_2)
          yield request
          
    def parse_2(self, response):
        for href in response.css("div.FeaturedHeader > h2 > a::attr('href')"):
          url = response.urljoin(href.extract())    
          request = scrapy.Request(url, callback=self.parse_dir_contents)
          yield request
          
    def parse_dir_contents(self, response):
        catalog = []
        contents = response.xpath('//*[@id="content_breadcrumb"]/li/a/img')
        for cont in contents:
          catalog.append(cont.xpath('@title').extract()[0])
          if catalog:
            items = []
            for sel in response.xpath('//div[@class="prod-data"]'):
              item = AllforyouItem()
            
              item['url'] = response.url or None
              item['title'] = sel.xpath('@data-name').extract()
              item['description'] = sel.xpath('@data-desc').extract()
              item['img_urls'] = sel.xpath('@data-imgurl').extract()
              item['quality'] = sel.xpath('@data-selqty').extract()
              item['price'] = sel.xpath('@data-price').extract()
              item['old_price'] = sel.xpath('@data-oldprice').extract()
              item['out_of_stock'] = sel.xpath('@data-outofstock').extract()
              items.append(item)
              yield item
            