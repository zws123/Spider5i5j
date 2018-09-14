# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import scrapy.http.response
from Spider5i5j.items import RoomInfoItem


class RoomspiderSpider(scrapy.Spider):
    name = 'roomspider'
    allowed_domains = ['bj.5i5j.com']
    # start_urls = ['http://bj.5i5j.com/']

    def start_requests(self):
        for page in range(1,self.settings.get('MAX_PAGE') + 1):
            url = 'https://bj.5i5j.com/zufang/haidianqu/u6n' + str(page) + '/'
            yield Request(url=url,callback=self.parse,meta={'url': url},dont_filter=True)

    def parse(self, response):
        requestURL = response.meta['url']
        str1 = '北京我爱我家'
        if str1 in response.text:
            item = RoomInfoItem()
            titles = response.css('li h3 a::text').extract()
            details = response.css('li .listX>p:first-child').xpath('./text()').extract()
            locations = response.css('li .listX>p:nth-child(2) a::text').extract()
            release_times = response.css('li .listX>p:nth-child(3)::text').re('.*\·\s(.*?)发布')
            rents = response.css('li .redC strong::text').extract()
            rent_catagorys = response.css('li .jia>p:nth-child(2)::text').re('出租方式：(.*)')
            for title,detail,location,release_time,rent,rent_catagory in zip(titles,details,locations,release_times,rents,rent_catagorys):
                item['title'] = title
                item['detail'] = detail
                item['location'] = location
                item['release_time'] = release_time
                item['rent']  = rent
                item['rent_catagory'] = rent_catagory
                yield item
        else:
            print('--------------------->>>>>>>>Your request is redirect,retrying.....<<<<<-------------------------')
            yield scrapy.Request(url=requestURL,meta={'url': requestURL}, callback=self.parse)

