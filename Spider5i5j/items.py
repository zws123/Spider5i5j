# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class RoomInfoItem(Item):
    collection = 'rooms'
    title = Field()
    detail = Field()
    location = Field()
    release_time = Field()
    rent = Field()
    rent_catagory = Field()


