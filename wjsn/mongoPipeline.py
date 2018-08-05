# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
from pymongo import MongoClient
from scrapy.exceptions import DropItem
import json

class mongoPipeline(object):

    def __init__(self):
        client = MongoClient('localhost',27017)
        db = client.test
        self.mes = db.mes


    def process_item(self, item, spider):
        text = dict(item)
        self.mes.insert(text)
        return item



'''
class mongoPipeline(object):

    def __init__(self):
        self.filename = open(r'F:\img\wjsn.json', "w")

        pass
    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.filename.write(text)
        return item

    def close_spider(self,spider):
        self.filename.close()
'''