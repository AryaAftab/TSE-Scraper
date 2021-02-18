# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    closingPriceData = scrapy.Field()
    bestLimitData = scrapy.Field()
    intraTradeData = scrapy.Field()
