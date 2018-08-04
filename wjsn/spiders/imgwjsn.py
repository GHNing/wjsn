# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from wjsn.items import WjsnItem


class ImgwjsnSpider(CrawlSpider):
    name = 'imgwjsn'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/f?kw=%E5%AE%87%E5%AE%99%E5%B0%91%E5%A5%B3&ie=utf-8&pn=0']

    pageLink = LinkExtractor(allow='kw=%E5%AE%87%E5%AE%99%E5%B0%91%E5%A5%B3&ie=utf-8&pn=\d+')

    rules = [
        Rule(pageLink, callback = 'parse_item', follow = True)
    ]

    def parse_item(self, response):
        inner_urls = response.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href').extract()
        urlhead = "http://tieba.baidu.com"
        for eachUrl in inner_urls:
            yield scrapy.Request(urlhead + str(eachUrl), callback=self.url_deail)
        '''
        item = WjsnItem()
        for each in response.xpath('//div[@class="t_con cleafix"]/div/div/div/a/text()').extract():
            item['title'] = each
            yield item
        '''
    def url_deail(self,response):
        rootUrl = response.url[-10:]
        imgurls = response.xpath('//img[@class="BDE_Image"]/@src').extract()
        for imgurl in imgurls:
            item = WjsnItem()
            item['imgurl'] = imgurl
            item['imgname'] = str(rootUrl)+"_"+str(imgurl[-12:-4])
            yield item
