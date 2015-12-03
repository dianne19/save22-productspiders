import scrapy
from save22_productspiders.items import Save22ProductspidersItem

class ExpansysItem(scrapy.Spider):
    name = "expansys"
    allowed_domains = ["expansys.com.sg"]
    start_urls = [
        "http://www.expansys.com.sg/mobile-phones/",
    ]

    def parse(self, response):
        for href in response.css("div#nav > ul.asia.me > li > a::attr('href')"):   
          url = response.urljoin(href.extract())
          request = scrapy.Request(url, callback=self.headd)
          yield request


    def headd(self, response):
        for href in response.css("div#product_listing > div.productGrid > ul.item.c0 > li.image > a::attr('href')"):
          url = response.urljoin(href.extract())
          request = scrapy.Request(url, callback=self.parse_dir_contents)
          yield request      

    def parse_dir_contents(self, response):
        items = list()