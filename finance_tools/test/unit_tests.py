import sys
import unittest

sys.path.append("../")
from modules.calculation.incomeStatement import OperatingExpenses, Revenue, IncomeStatement
from modules.calculation.balanceSheet import BalanceSheet
import random
import string
import time
import datetime
import json

from bson.objectid import ObjectId


class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return o.__dict__


class TestBalanceSheet(unittest.TestCase):

    def get_random_int(self, min=0, max=sys.maxsize):
        return random.randint(min, max)

    def test_balance_sheet(self):
        company_name = "".join(random.choice(string.ascii_letters) for x in range(random.randint(1, 15)))
        date = int(time.time())
        cash = self.get_random_int()
        short_term_investment = self.get_random_int()
        net_receivable = self.get_random_int()
        inventory = self.get_random_int()
        other_current_assets = self.get_random_int()
        long_term_investment = self.get_random_int()
        property_plant_equipment = self.get_random_int()
        goodwill = self.get_random_int()
        intangible_assets = self.get_random_int()
        amortization = self.get_random_int()
        other_assets = self.get_random_int()
        deferred_long_term_assets_change = self.get_random_int()
        accounts_payable = self.get_random_int()
        short_debt = self.get_random_int()
        other_current_liabilities = self.get_random_int()
        long_term_debt = self.get_random_int()
        other_liabilities = self.get_random_int()
        deferred_long_term_liability = self.get_random_int()
        minority_interest = self.get_random_int()
        negative_goodwill = self.get_random_int()
        misc_stocks_options_warrants = self.get_random_int()
        redeemable_preferred_stock =self.get_random_int()
        preferred_stock =self.get_random_int()
        common_stock = self.get_random_int()
        retained_earnings = self.get_random_int()
        treasury_stock = self.get_random_int()
        capital_surplus = self.get_random_int()
        other_stockholder_equity = self.get_random_int()
        balance_sheet = BalanceSheet(company_name,
                 date,
                 cash,
                 short_term_investment,
                 net_receivable,
                 inventory,
                 other_current_assets,
                 long_term_investment,
                 property_plant_equipment,
                 goodwill,
                 intangible_assets,
                 amortization,
                 other_assets,
                 deferred_long_term_assets_change,
                 accounts_payable,
                 short_debt,
                 other_current_liabilities,
                 long_term_debt,
                 other_liabilities,
                 deferred_long_term_liability,
                 minority_interest,
                 negative_goodwill,
                 misc_stocks_options_warrants,
                 redeemable_preferred_stock,
                 preferred_stock,
                 common_stock,
                 retained_earnings,
                 treasury_stock,
                 capital_surplus,
                 other_stockholder_equity)

        self.assertTrue(False == balance_sheet.verify(), "balance sheet is not equal")


class TestIncomeStatement(unittest.TestCase):

    def test_revenue(self):
        income = 10000
        cogs = 500
        expected_result_margin = float(income - cogs)/float(income)
        expected_result_profit = income-cogs
        revenue = Revenue(income, cogs)
        self.assertEqual(revenue.get_margin(), expected_result_margin, "Should be %f" % expected_result_margin)
        self.assertEqual(revenue.gross_profit, expected_result_profit, "Should be %f" % expected_result_profit)

    def test_operating_expense(self):
        r_and_d = 1000
        selling_g_and_admin = 100
        non_recurring = 200
        others = 100
        expected = r_and_d + selling_g_and_admin + non_recurring + others
        operating_expense = OperatingExpenses(r_and_d, selling_g_and_admin, non_recurring, others)
        self.assertEqual(operating_expense.get_total(), expected, "Should be %f" % expected)

    def test_full_income_statement(self):
        total_revenue = 10000
        cost_of_revenue = 500
        research_development = 200
        selling_general_and_administrative = 100
        non_recurring = 20
        others = 30
        other_expense_or_income = 10
        interest_expense = 0
        income_tax_expense = 10

        income_statement = IncomeStatement(total_revenue,
                                           cost_of_revenue,
                                           research_development,
                                           selling_general_and_administrative,
                                           non_recurring,
                                           others,
                                           other_expense_or_income,
                                           interest_expense,
                                           income_tax_expense)

        print(JSONEncoder().encode(income_statement))

        expected = total_revenue - \
                   cost_of_revenue - \
                   research_development - \
                   selling_general_and_administrative - \
                   non_recurring - \
                   others - \
                   other_expense_or_income - \
                   interest_expense - \
                   income_tax_expense

        operating_expense = income_statement.operating_expense.get_total()
        expected_operating = research_development + selling_general_and_administrative + others + non_recurring

        self.assertEqual(operating_expense, expected_operating,
                         "Operating expense %s " % income_statement.operating_expense.get_total())

        expected_other_income = other_expense_or_income + interest_expense + income_tax_expense
        self.assertEqual(income_statement.other_income_or_expense.get_total(),
                         expected_other_income,
                         "Should be %f, actual was : %f " % (expected_other_income,
                                                             income_statement.other_income_or_expense.get_total()))

        self.assertEqual(income_statement.net_income,
                         expected,
                         "Should be %f, actual was : %f " % (expected, income_statement.net_income))

        expected_profit_margin = float(expected) / float(total_revenue)
        self.assertEqual(income_statement.get_net_profit_margin(),
                         expected_profit_margin,
                         "profit margin should be %f" % expected_profit_margin)

        expected_operating_margin = float(total_revenue - \
                                     cost_of_revenue - \
                                     research_development - \
                                     selling_general_and_administrative - \
                                     non_recurring - \
                                     others) / float(total_revenue)

        self.assertEqual(income_statement.get_operating_profit_margin(),
                         expected_operating_margin,
                         "expected operating margin should be %f" % expected_operating_margin)

if __name__ == '__main__':
    unittest.main()