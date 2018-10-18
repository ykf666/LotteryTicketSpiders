# -*- coding: utf-8 -*
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from LotteryTicket.items import LotteryticketItem


class LCWSpider(CrawlSpider):
    name = "lcw"

    allowed_domains = ["17500.cn"]

    start_urls = [
        "http://www.17500.cn/ssq/all.php"
    ]

    rules = [
        Rule(LinkExtractor(allow=('/ssq/details.php\?issue=(\d{7})',)), callback='parse_page')
    ]

    @staticmethod
    def parse_page(response):
        hxs = HtmlXPathSelector(response)
        item = LotteryticketItem()
        # 期数
        title = hxs.select('//html/body/center/center/table/tr/td/table[1]/tr[2]/td[1]/text()').extract()[0]
        title = filter(str.isdigit, "".join(title.split()))
        item['title'] = "".join(list(title))
        # 红色球区
        red1 = hxs.select('//html/body/center/center/table/tr/td/table[2]/tbody/tr[2]/td[1]/font/text()').extract()[0]
        red1 = filter(str.isdigit, "".join(red1.split()))
        item['red1'] = "".join(list(red1))
        red2 = hxs.select('//html/body/center/center/table/tr/td/table[2]/tbody/tr[2]/td[2]/font/text()').extract()[0]
        red2 = filter(str.isdigit, "".join(red2.split()))
        item['red2'] = "".join(list(red2))
        red3 = hxs.select('//html/body/center/center/table/tr/td/table[2]/tbody/tr[2]/td[3]/font/text()').extract()[0]
        red3 = filter(str.isdigit, "".join(red3.split()))
        item['red3'] = "".join(list(red3))
        red4 = hxs.select('//html/body/center/center/table/tr/td/table[2]/tbody/tr[2]/td[4]/font/text()').extract()[0]
        red4 = filter(str.isdigit, "".join(red4.split()))
        item['red4'] = "".join(list(red4))
        red5 = hxs.select('//html/body/center/center/table/tr/td/table[2]/tbody/tr[2]/td[5]/font/text()').extract()[0]
        red5 = filter(str.isdigit, "".join(red5.split()))
        item['red5'] = "".join(list(red5))
        red6 = hxs.select('//html/body/center/center/table/tr/td/table[2]/tbody/tr[2]/td[6]/font/text()').extract()[0]
        red6 = filter(str.isdigit, "".join(red6.split()))
        item['red6'] = "".join(red6)
        # 蓝色球区
        blue = hxs.select('//html/body/center/center/table/tr/td/table[2]/tbody/tr[2]/td[7]/font/text()').extract()[0]
        blue = filter(str.isdigit, "".join(blue.split()))
        item['blue'] = "".join(list(blue))
        # 开奖时间
        created_at = hxs.select('//html/body/center/center/table/tr/td/table[1]/tr[2]/td[2]/text()').extract()[0]
        item['created_at'] = ("".join(created_at.split()))[0:10]

        return item
