# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wjsn.items import WjsnItem

class MongowjsnSpider(CrawlSpider):
    name = 'mongoWjsn'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/f?kw=%E5%AE%87%E5%AE%99%E5%B0%91%E5%A5%B3&ie=utf-8&pn=0']

    pageLink = LinkExtractor(allow='kw=%E5%AE%87%E5%AE%99%E5%B0%91%E5%A5%B3&ie=utf-8&pn=\d+')

    rules = [
        Rule(pageLink, callback='json_item', follow=True)
    ]

    def json_item(self, response):
        url = 'http://tieba.baidu.com'
        mes = response.xpath('//div[@class="t_con cleafix"]/div/div/div/a')
        for each in mes:
            item = WjsnItem()
            item['title'] = each.xpath('./text()').extract()[0]
            item['parentUrl'] = url + str(each.xpath('./@href').extract()[0])
            yield item

    def parse_item(self, response):
        pass
