from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request,FormRequest
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import XmlXPathSelector
from scrapy.linkextractors import LinkExtractor
import json
import re
import uuid
import hashlib
import logging
import subprocess
import requests
import csv
import io
import scrapy
from datetime import datetime
import os
class ShalmanaSpider(scrapy.Spider):
    name = "shalmana"
    allowed_domains = []
    start_urls = ['http://www.shalmana.com/preowned-cars/?order=-price&per_page=12']

    def parse(self, response):
        sel = Selector(response)
        cars = sel.xpath('//div[@class="listing module used-list standard-list"]/div/div')
        print(len(cars))