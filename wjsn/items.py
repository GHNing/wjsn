# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WjsnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    imgurl = scrapy.Field()
    imgname = scrapy.Field()
    #mongoWjsn
    parentUrl = scrapy.Field()
    title = scrapy.Field()

    #http://m.api.xingyan.panda.tv/room/list?pagenum=2&xtype=1
