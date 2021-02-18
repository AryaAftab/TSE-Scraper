# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from product_scraper.items import ProductScraperItem
import time
import re
from datetime import datetime, timedelta



def links(first_link, days):
    AllLinks = []
    Delta = timedelta(days=1)
    Now = datetime.today()

    for counter in range(days):

        Now = Now - Delta
        AllLinks.append(first_link + '{:0>4d}{:0>2d}{:0>2d}'.format(Now.year, Now.month, Now.day))
    return AllLinks

class MySpider(scrapy.Spider):
    name = 'myspider'

    first_link = "http://cdn.tsetmc.com/Loader.aspx?ParTree=15131P&i=114312662654155&d="
    start_urls = links(first_link, 180)


    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                endpoint='render.html',
                args={'wait': 0.5},
            )


    
    def parse(self, response):
        item = ProductScraperItem()
        item['url'] = response.url

        buff = response.xpath('//*[@id="MainContent"]/script[1]/text()').get()
        try:
            pattern = "ClosingPriceData=\[\[(.*?)\]\];"
            item['closingPriceData'] = re.findall(pattern, buff)[0]
        except:
            item['closingPriceData'] = []

        try:
            pattern = "IntraTradeData=\[\[(.*?)\]\];"
            item['intraTradeData'] = re.findall(pattern, buff)[0]
        except:
            item['intraTradeData'] = []

        buff = response.xpath('//*[@id="MainContent"]/script[2]/text()').get()
        try:
            pattern = "BestLimitData=\[\[(.*?)\]\];"
            item['bestLimitData'] = re.findall(pattern, buff)[0]
        except:
            item['bestLimitData'] = []
        #item['price'] = response.text
        print('*' * 70)
        return item