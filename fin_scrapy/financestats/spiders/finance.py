# -*- coding: utf-8 -*-
import json

import scrapy
from utils.mongohandler import *

from . import parser
from . import utils

MONGO_ADDRESS = 'mongodb://localhost:27017/'

MONGO_CONNECTION = Mongo_Client_Wrapper(MONGO_ADDRESS)

class FinanceClassicSpider(scrapy.Spider):
    def __init__(self, tickers):
        self.ticker_stocks = tickers

    name = 'finance'
    allowed_domains = ['finance.yahoo.com']

    def start_requests(self):
        print((self.ticker_stocks))

        stocks = self.ticker_stocks.split(',')

        for stock in stocks:
            print(("yield %s" % (stock)))
            url = "http://finance.yahoo.com/quote/{0}?p={1}".format(stock, stock)
            request = scrapy.Request(url=url, callback=self.parse_stock_page)
            request.meta["stock"] = stock
            yield request

    @staticmethod
    def yield_request(full_url, callback_func):
        req = scrapy.Request(url=full_url, callback=callback_func)
        return req

    def parse_key_stats_page(self, response):
        print("in key stats page")
        rows = response.xpath('//table//tr')
        for row in rows[1:]:
            data = {
                row.xpath('td[1]//text()').extract_first(): {row.xpath('td[2]//text()').extract_first(),
                                                             row.xpath('td[3]//text()').extract_first(),
                                                             row.xpath('td[4]//text()').extract_first(),
                                                             row.xpath('td[5]//text()').extract_first()}

            }

        summary_data = response.meta["context"]
        summary_data.update(data)

        other_details_json_link = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/{0}?formatted=true&" \
                                  "lang=en-US&region=US&modules=summaryProfile%2CfinancialData%2CrecommendationTrend" \
                                  "%2CupgradeDowngradeHistory%2Cearnings%2CdefaultKeyStatistics" \
                                  "%2CcalendarEvents%2CsummaryDetail%2Cprice%2CincomeStatementHistory" \
                                  "%2CcashflowStatementHistory" \
                                  "%2CbalanceSheetHistory&corsDomain=finance.yahoo.com".format(
            response.meta["stock"])

        request = self.yield_request(other_details_json_link, self.parse_json)
        request.meta["context"] = summary_data
        request.meta["stock"] = response.meta["stock"]
        yield request

    def parse_stock_page(self, response):
        print("in parse stock page")
        summary_table = response.xpath('//div[contains(@data-test,"summary-table")]//tr')

        summary_data = utils.parse_dom_table(summary_table)
        stats_url = "https://finance.yahoo.com/quote/AAPL/key-statistics?p=%s" % (response.meta["stock"])

        request = self.yield_request(stats_url, self.parse_key_stats_page)
        request.meta["context"] = summary_data
        request.meta["stock"] = response.meta["stock"]
        yield request


    def parse_json(self, response):
        print("parse json")
        data_context = {}
        ticker = response.meta['stock']
        try:
            json_loaded_summary = json.loads(response.text)
            json_result = json_loaded_summary["quoteSummary"]["result"][0]

            data_context["summary_data"] = parser.parse_summary_data(json_result,
                                                                     response.meta['context'],
                                                                     response.url,
                                                                     ticker)

            data_context["cash_flow"] = parser.parse_cash_flow_statement(json_result, ticker)
            data_context["balance_sheet"] = parser.parse_balance_sheet(json_result, ticker)
            print(("balance sheets %s" % len(data_context["balance_sheet"])))
            data_context["income_statement"] = parser.parse_income_statement(json_result, ticker)

        except Exception as e:
            print(e)
            print ("Failed to parse json response")

        insert_data_into_mongo(data_context)


def insert_data_into_mongo(context):
    print("insert data into mongo")
    print((type(context)))
    for key, value in list(context.items()):
        print(("inserted %s" % value))
        if type(value) is list:
            for item in value:
                MONGO_CONNECTION.mongo_insert(key, dict(item))
        else:
            MONGO_CONNECTION.mongo_insert(key, dict(value))
