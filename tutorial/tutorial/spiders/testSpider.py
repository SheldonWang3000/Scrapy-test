__author__ = 'Teer'
# -*- coding: utf-8 -*-
# bbsSpider, Created on Oct, 2014
# version:
# author: chenqx @http://chenqx.github.com
# See more: http://doc.scrapy.org/en/latest/index.html

from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from tutorial.items import TutorialItem
import chardet


class TestSpider(CrawlSpider):
    name = 'testSpider'
    # all = 0
    allow_domain = ['http://wz.sun0769.com/']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4']
    # rules = {
    #     Rule(LxmlLinkExtractor(allow='page')),
    #     # Rule(LxmlLinkExtractor(allow='/index\.php/question/questionType\?type=4$')),
    #     Rule(LxmlLinkExtractor(allow='/html/question/\d+/\d+\.shtml$'), callback='parse_content')
    # }
    _x_query = {
        'title': '''//div[contains(@class, 'pagecenter p3')]/div/div/div[contains(@class,'cleft')]/strong/text()''',
        'content': '''//div[contains(@class, 'c1 text14_2')]/text()''',
        'content_first': '''//div[contains(@class, 'contentext')]/text()'''
    }

    def parse(self, response):
        links = LxmlLinkExtractor(allow='/html/question/\d+/\d+\.shtml$').extract_links(response)
        links += LxmlLinkExtractor(allow='/index\.php/question/show\?id=\d+$').extract_links(response)
        for link in links:
            yield Request(url=link.url, callback=self.parse_content)
        sel = Selector(response)
        next_page = sel.xpath('''//div[contains(@class, 'pagination')]/a/@href''').extract()[-2]
        yield Request(url=next_page)
        # links = LxmlLinkExtractor().extract_links(response)
        # for link in links:
        #     print link
        # print '------------'
        # return CrawlSpider.parse(self, response)

    def parse_content(self, response):
        bbs_item_loader = ItemLoader(item=TutorialItem(), response=response)
        url = response.url
        html = response.body
        bbs_item_loader.add_value('url', url)
        bbs_item_loader.add_value('html', html)

        return bbs_item_loader.load_item()
