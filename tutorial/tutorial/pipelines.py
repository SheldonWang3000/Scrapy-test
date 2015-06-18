# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import os
from scrapy.contrib.exporter import JsonLinesItemExporter, XmlItemExporter


class XmlWritePipeline(object):
    def __init__(self):
        self.num = 0
        pass

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        print 'open'
        # self.file = open(spider.name + '.txt', 'wb')
        # self.expoter = JsonLinesItemExporter(self.file, ensure_ascii=False)
        # # self.expoter = XmlItemExporter(self.file)
        # self.expoter.start_exporting()

    def spider_closed(self, spider):
        print 'close'
        # self.expoter.finish_exporting()
        # self.file.close()

        # process the crawled data, define and call dataProcess function
        # dataProcess('bbsData.xml', 'text.txt')

    def process_item(self, item, spider):
        # self.expoter.export_item(item)
        # print os.getcwd()
        # raw_input("Press Enter to continue...")
        # f = open(os.getcwd() + '/' + item['url'][0] + '.txt', 'wb')
        path = 'page/' + str(self.num) + '.txt'
        self.num += 1
        f = open(path, 'wb')
        f.write(item['html'][0])
        f.close()
        # raw_input('wait')
        return item
