# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HrspiderItem(scrapy.Item):
    # define the fields for your item here like:
    BGName = scrapy.Field()
    CategoryName = scrapy.Field()
    CountryName = scrapy.Field()
    Id = scrapy.Field()
    IsCollect = scrapy.Field()
    IsValid = scrapy.Field()
    LastUpdateTime = scrapy.Field()
    LocationName = scrapy.Field()
    PostId = scrapy.Field()
    PostURL = scrapy.Field()
    ProductName = scrapy.Field()
    RecruitPostId = scrapy.Field()
    RecruitPostName = scrapy.Field()
    Responsibility = scrapy.Field()
    SourceID = scrapy.Field()
    Requirement = scrapy.Field()
