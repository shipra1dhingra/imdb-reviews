import scrapy
from scrapy import *
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
from scrapy.http import Request,FormRequest
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import XmlXPathSelector
from scrapy.linkextractors import LinkExtractor
class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_urls=[]
    start_url=['https://medium.com/']

    def home(self, response):
        sel = Selector(response)
        home_link = ''.join(sel.xpath('//a[@class="df-link ds-link--stylePointer"]/a/@href').extract()).strip()
        print("home page ccontent",home_link)
    def parse(self, response):
        sel=Selector(response)
        medium_content=''.join(sel.xpath('//div[@class="screenContent surface-content"]' ).extract()).strip()
        print("medium content size",len(medium_content))
        yield Request(medium_content, callback=self.parse, dont_filter=True)
    def relation_article(self,response):
        sel=Selector(response)
        relationships=''.join(sel.xpath('//a[@class="ds-link ds-link styleSubtle uicapsSubtle"]/a/@href').extract()).strip()
        relationships_content=''.join(sel.xpath('//h2[@class="bc db bd fm fn fo ar am fp fq fr"]/text()').extract()).strip()
        relationships_content1 = ''.join(sel.xpath('//h2[@class="fs ft n"]/text()').extract()).strip()
        #print(f"relationship {relationships} relationship latest content{relationships_content}{relationships_content1}")
    def business_article(self, response):
        sel = Selector(response)
        business_1= ''.join(sel.xpath('//a[@class="ds-link ds-link--styleSubtle uicapsSubtle"]/a/@href').extract()).strip()
        business_content = ''.join(sel.xpath('//h2[@class="bc db bd ff fg fh ar am fi fj fk"]/text()').extract()).strip()
        business_content1=''.join(sel.xpath('//div[@class="fl fm n"]/text()').extract()).strip()
        #print(f"business{business_1} business latest content{business_content}{business_content1}")

    def recent_read(self,response):
        sel = Selector(response)
        reading_histoy=''.join(sel.xpath('//span[@class="ui-capsSubtle"]/text()').extract()).strip()
        print(f"based on your recent history{reading_histoy}")
    def style_(self,response):
        sel = Selector(response)
        style= ''.join(sel.xpath('//a[@class="ds-link ds-link--styleSubtle uicapsSubtle"]/a/@href').extract()).strip()
        style_latest = ''.join(sel.xpath('//h2[@class="bc db bd ff fg fh ar am fi fj fk"]/text()').extract()).strip()
        style_content1 = ''.join(sel.xpath('//div[@class="fl fm n"]/text()').extract()).strip()
        print(f"style{style} latest style content{style_latest}{style_content1}")
    def featured(self,response):
        sel = Selector(response)
        see_all_featured=''.join(sel.xpath('//a[@class="ds-link ds-link--styleObvious ui-caption ui-caps"]/a/@href').extract()).strip()
        featured_stories = ''.join(sel.xpath('//h2[@class="ar am da bc db bd dc dd de at aw df dgdh av"]/text()').extract()).strip()
        latest_stories=''.join(sel.xpath('//div[@class="fj fk n"]/text()').extract()).strip()
        print(f"See all featured stories {see_all_featured}{featured_stories} latest stories{latest_stories}")

    def ONEZERO(self, response):
        sel = Selector(response)
        ONEZERO_ =''.join(sel.xpath('//spam[@class="ds-nav-text"/text()').extract()).strip()
        for i in ONEZERO_:
           url='https://medium.com/'+''.join(i.xpath('//a[@class="link link--darken u-accentColor--textDarken link--noUnderline u-baseColor--link js-navItem is-touched"]/a/@href').extract()).strip()
           print(f"urls of ONEZERO the content Consumer tech,Digital life,Industry,Science&medicine,About{url}")
           print(f"urls of ELEMENTAL {url}")
           print(f"GEN{url}")
           print(f"startups{url}")
           print(f"SELF",{url})
           print(f"TECH",{url})
           print(f"HEATED",{url})
           print(f"Zora",{url})
    def explore(self,response):
        sel=Selector(response)
        explore_=''.join(sel.xpath('//h1[@class="u-fontSize32 u-xs-fontSize24 u-fontWeightBold u-textColorDarkest u-letterSpacing003 u-paddingBottoms"/text()').extract()).strip()
        print("to explore more",explore_)
        for j in explore_:
         content_explore = ''.join(j.xpath('//a[@class="link link--noUnderline u-baseColor--link u-flex1 u--uiDisplayBold u-fontSize20 is-touched"/text()').extract()).strip()
         print("Art"
               "beauty"
               "comics"
               "books"
               "culture"
               "fiction"
               "food"
               "film"
               "music gaming"
               "and many more...",content_explore)