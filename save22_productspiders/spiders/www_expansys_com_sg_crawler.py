from datetime import datetime

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from save22_productspiders.items import Save22ProductspidersItem


class WwwExpansysComSgCrawler(CrawlSpider):
  name = 'www_expansys_com_sg_crawler'
  allowed_domains = ['expansys.com.sg']
  start_urls = [
      'http://www.epansys.com.sg/mobile-phones/'
      ]
  
  rules = (
    Rule(
      LinkExtractor(
        allow = (r'(.+)',),
        ),
        callback = 'parse_item',
    ),
  )
  
  def parse_item(self,response):
    for href in response.css("div#product_listing > div.productGrid > ul.item.c0 > li.image > a::attr('href')"):
          url = response.urljoin(href.extract())
          print url
          yield request
    pass