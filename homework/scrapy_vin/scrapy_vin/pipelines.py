# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json 
class ScrapyVinPipeline(object):
    def process_item(self, item, spider):
        object_ = json.dump(dict(item)) + "\n"
        self.write(object_)
        return item
            
    def open_spider(self, spider):
        self.file = open('homework\scrapy_vin\items.json', 'a+')
    
    def close_spider(self, spider):
        self.file.close()

 