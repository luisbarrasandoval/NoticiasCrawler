# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from yaml import serialize

class NoticiasItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    img = scrapy.Field()
    description = scrapy.Field()
    author = scrapy.Field()
    publish_date = scrapy.Field(
        serializer=str
    )
    category = scrapy.Field()
    content = scrapy.Field()
    
