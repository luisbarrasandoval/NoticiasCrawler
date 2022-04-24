# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from attr import field
import scrapy
from dataclasses import dataclass
from datetime import datetime

@dataclass
class NoticiasItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title: str
    author: str
    content: str
    category: list[str] = field(serializer=str)
    publish_date: datetime = field(serializer=str)
