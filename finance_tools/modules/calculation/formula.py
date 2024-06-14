def get_current_ratio(total_current_assest, total_current_liabillities):
    return float(total_current_assest) / float(total_current_liabillities)


def get_quick_ratio(total_current_assest, total_current_liabillities, inventories):
    return float(total_current_assest - inventories) / float(total_current_liabillities)


def get_debt_to_equity(debt, equity):
    return float(debt) / float(equity)


def get_gross_profit_margin(gross_profit, revenue):
    return float(gross_profit) / float(revenue)


def get_operating_margin(operating_income, revenue):
    return float(operating_income) / float(revenue)


def get_net_profit_margin(net_income, revenue):
    return float(net_income) / float(revenue)


def get_cash_flow_from_operations_ratio(cash_from_operation, revenue):
    return float(cash_from_operation) / float(revenue)


def get_return_on_assets(net_income, assets):
    return float(net_income) / float(assets)


def get_return_on_equity(net_income,
                         short_term_investment,
                         long_term_debt,
                         current_portion_long_term_debt,
                         cash_and_equiv,
                         total_equity):
    return float(net_income) / \
           float(
               total_equity + long_term_debt + current_portion_long_term_debt - cash_and_equiv - short_term_investment)


def get_cash_flow_from_operation_to_net_income_ratio(cash_flow_from_opeartion, net_income):
    return float(cash_flow_from_opeartion) / float(net_income)


def get_days_sales_outstanding(accounts_receivable, revenue):
    return 365 * (float(accounts_receivable) / float(revenue))


def get_inventory_turn_over(inventories, cogs):
    return float(inventories) / float(cogs)


def get_days_payable_outstanding(accounts_payable, beginning_inventory, cogs, ending_inventory):
    return float(accounts_payable) / float(ending_inventory + cogs - beginning_inventory)


def get_days_of_inventory_outstanding(beginning_inventory, ending_inventory, cogs):
    average_inevntory = (beginning_inventory + ending_inventory) / 2.0
    return cogs / average_inevntory


def get_cash_conversion_cycle(dio, dso, dpo):
    return dio + dso - dpo


def get_interest_coverage_ratio(net_interest, operating_income):
    return float(operating_income) / float(net_interest)
