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
          request = scrapy.Request(url, callback=self.parse_2)
          yield request


    def parse_2(self, response):
        for href in response.css("div#product_listing > div.productGrid > ul.item.c0 > li.image > a::attr('href')"):
          url = response.urljoin(href.extract())
          request = scrapy.Request(url, callback=self.parse_dir_contents)
          yield request      

    def parse_dir_contents(self, response): 
      items = list()

          for sel in response.xpath('//div[@class="prod_head"]'):
            item = Save22ProductspidersItem()
            
              item['Link'] = response.url or None
          #    item['Title'] = sel.xpath('@data-name').extract()
          #    item['Description'] = sel.xpath('@data-desc').extract()
           #   item['Image_Link'] = sel.xpath('@data-imgurl').extract()
          #    item['Quality'] = sel.xpath('@data-selqty').extract()
           #   item['Price'] = sel.xpath('@data-price').extract()
            #  item['Old_price'] = sel.xpath('@data-oldprice').extract()
             # item['Out_of_stock'] = sel.xpath('@data-outofstock').extract()
            #  items.append(item)
             # yield item