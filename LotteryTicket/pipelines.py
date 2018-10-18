# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.exceptions import DropItem
from scrapy.conf import settings


class LotteryticketPipeline(object):
    def __init__(self):
        self.server = settings['MONGODB_SERVER']
        self.port = settings['MONGODB_PORT']
        self.db = settings['MONGODB_DB']
        self.col = settings['MONGODB_COLLECTION']
        client = MongoClient(self.server, self.port)
        db = client[self.db]
        self.collection = db[self.col]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("丢失%s期开奖数据" % item['title'])

        if valid:
            self.collection.insert_one(dict(item))
        return item