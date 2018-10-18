# -*- coding: utf-8 -*-

# Scrapy settings for LotteryTicket project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'LotteryTicket'

SPIDER_MODULES = ['LotteryTicket.spiders']
NEWSPIDER_MODULE = 'LotteryTicket.spiders'

ITEM_PIPELINES = {'LotteryTicket.pipelines.LotteryticketPipeline':10}
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27117
MONGODB_DB = "lottery_ticker"
MONGODB_COLLECTION = "shuangseqiu"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) '\
    'Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = False