from .calculation.balanceSheet import BalanceSheet


class Comapny:
    def __init__(self, company_name, date, balance_sheet, income_statement, cash_flow):
        self.company_name = company_name
        self.date = date
        self.balance_sheet = balance_sheet
        self.income_statement = income_statement
        self.cash_flow = cash_flow


def init_company_stats(date,
                       company_name,
                       total_revenue,
                       cost_of_revenue,
                       research_development,
                       selling_general_and_administrative,
                       non_recurring,
                       others,
                       other_expense_or_income,
                       interest_expense,
                       income_tax_expense,
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
                       other_stockholder_equity):
    income_statement = IncomeStatemnt(total_revenue,
                                      cost_of_revenue,
                                      research_development,
                                      selling_general_and_administrative,
                                      non_recurring,
                                      others,
                                      other_expense_or_income,
                                      interest_expense,
                                      income_tax_expense)

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

    return Comapny(company_name, date, balance_sheet, income_statement, None)
