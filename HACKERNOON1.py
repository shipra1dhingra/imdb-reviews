import scrapy
from scrapy import *
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
from scrapy.http import Request,FormRequest
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import XmlXPathSelector
from scrapy.linkextractors import LinkExtractor
class SpiderSpider(scrapy.Spider):
    name = 'hackernoon'
    allowed_urls=[]
    start_url=[' https://hackernoon.com/?gi=2ed357c707eb']
    def hack(self,response):
        #sel=scrapy.Selector(response)
        page_content=''.join(response.xpath('//div[@class="screenContent surface-Content"]/text()').extract()).strip()
        for i in page_content:
         make=''.join(i.xpath('//div[@class="u-letterSpacingTight u-lineHeightTighter u-breakWord u-textOverflowEllipsis u-lineClamp3 u-fontSize24"]/text()').extract()).strip()
         print("NEWS HEADINGS",make)
    def latest(self,response):
        sel = scrapy.Selector(response)
        latest_news_head = ''.join(sel.xpath('//span[@class="heading-title heading-title--darkheading-title--lineHeightTight u-fontSize18 u-contentSansThin"]').extract()).strip()
        for j in latest_news_head:
            latest_news_headings = ''.join(j.xpath('//div[@class="u-paddingBottom15 js-trackpostPresentation"]/text()').extract()).strip()
            print("LATEST NEW HEADINGS ON HACKERNOON.COM",latest_news_headings)

    def other(self, response):
        sel = scrapy.Selector(response)
        top_and_other = ''.join(sel.xpath('//div[@class="screenContent surface-Content"]/text()').extract()).strip()
        for k in top_and_other:
            url="https://hackernoon.com/?gi=2ed357c707e"+''.join(k.xpath('a[@class="link link--darken u-accentColor--textDarken link--noUnderline u-BaseColor--link js-navItemLink is-touched"]/a/@href').extract()).strip()
            print("links for ","LATEST NEWS"
                                "TOP NEWS"
                                "83 VC FIRMS"
                                "GET PUBLISHED"
                                "DEV"
                                "POD"
                                "AI"
                               "JOIN COMMUNITY",url)
            pass
