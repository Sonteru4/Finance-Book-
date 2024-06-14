import os
import time

import logger
from app import mongo
from modules.calculation.balanceSheet import BalanceSheet

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))


def build_balance_sheet(doc):
    return BalanceSheet(doc["ticker"],
                        time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(doc["endDate"])),
                        float(doc["cash"]),
                        float(doc["shortTermInvestments"]),
                        float(doc["netReceivables"]),
                        float(doc["inventory"]),
                        float(doc["otherCurrentAssets"]),
                        float(doc["totalCurrentAssets"]),
                        float(doc["longTermInvestments"]),
                        float(doc["propertyPlantEquipment"]),
                        float(doc.get("goodWill", 0)),
                        float(doc.get("intangibleAssets", 0)),
                        float(doc.get("amortization", 0)),
                        float(doc["otherAssets"]),
                        float(doc["totalAssets"]),
                        float(doc.get("deferredLongTermAssetCharges", 0)),
                        float(doc["accountsPayable"]),
                        float(doc.get("shortLongTermDebt", 0)),
                        float(doc["otherCurrentLiab"]),
                        float(doc["totalCurrentLiabilities"]),
                        float(doc["longTermDebt"]),
                        float(doc["otherLiab"]),
                        float(doc.get("deferredLongTermLiab", 0)),
                        float(doc.get("minorityInterest", 0)),
                        float(doc.get("negativeGoodwill", 0)),
                        float(doc["totalLiab"]),
                        float(doc.get("misc.StocksOptionsWarrants", 0)),  # TODO : find company with options
                        float(doc.get("redeemablePreferredStock", 0)),  # TODO : find company with options
                        float(doc.get("preferredStock", 0)),
                        float(doc["commonStock"]),
                        float(doc["retainedEarnings"]),
                        float(doc["treasuryStock"]),
                        float(doc.get("capitalSurplus", 0)),
                        float(doc["otherStockholderEquity"]))


def get_company_data(ticker):
    cursor = mongo.balance_sheet.find({"ticker": ticker})
    balances = []
    for doc in cursor:
        balance = build_balance_sheet(doc)
        LOG.info(balance.verify())
        LOG.info(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(doc["endDate"])))
        LOG.info("current ratio : %s " % balance.get_current_ratio())
        LOG.info("quick ratio : %s " % balance.get_quick_ratio())
        LOG.info("debt to equity : %s " % balance.get_debt_to_equity())
        LOG.info("enterprise value : %s " % balance.get_net_working_capital())
        balances.append(balance)
    return balances
