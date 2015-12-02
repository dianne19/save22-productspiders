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
  
      
def parse(self, response):
  for href in response.css("div.span2.categorybox-span > div.categorybox.thumbnail.text-center > div.thumb > a::attr('href')"):
    url = response.urljoin(href.extract())
    print url
    request = scrapy.Request(url, callback=self.parse_2)
    yield request

def parse_2(self, response):
    for href in response.css("div.FeatueredHeader > h2 > a::attr('href')"):
    url = response.urljoin(href.extract())
    request = scrapy.Request(url, callback=self.parse_dir_contents)
    yield request


def parse_dir_contents(self, response):
    for sel in response.xpath('//div#prod-data-id126641.prod-data'):
    item = AllforYouItem()
    item['name'] = sel.xpath('text()').extract()
    item['title'] = response.xpath = ('//*[id="product"]/*[@id="title"]/h3/text()'.extract()
    item['link'] = sel.xpath('a/@href').extract()
    item['desc'] = sel.xpath('text()').extract()
    yield item