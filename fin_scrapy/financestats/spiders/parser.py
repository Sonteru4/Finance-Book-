from . import utils


def format_earnings_list(earnings_raw):
    datelist = []
    for i in earnings_raw['earningsDate']:
        datelist.append(i['fmt'])
    earnings_date = ' to '.join(datelist)
    return earnings_date


def parse_balance_sheet(json_raw_result, ticker):
    balance_sheets = []
    balance_sheet = json_raw_result["balanceSheetHistory"]["balanceSheetStatements"]
    print(("len %s" % len(balance_sheet)))
    for i in balance_sheet:
        balance_sheet_data = utils.raw_json_answer_parser(i)
        balance_sheet_data['ticker'] = ticker
        balance_sheets.append(balance_sheet_data)
    return balance_sheets


def parse_summary_data(json_raw_result, summary_data, url, stock):
    summary_detail = json_raw_result["summaryDetail"]
    summary_detail_data = utils.raw_json_answer_parser(summary_detail)

    recommendation_trend_data = utils.raw_json_answer_parser(json_raw_result["recommendationTrend"])

    price_data = utils.raw_json_answer_parser(json_raw_result["price"])
    earnings_date = format_earnings_list(json_raw_result["calendarEvents"]['earnings'])

    summary_data.update(
        {'1y Target Est': json_raw_result["financialData"]["targetMeanPrice"]['raw'],
         'EPS (TTM)': json_raw_result["defaultKeyStatistics"]["trailingEps"]['raw'],
         'Earnings Date': earnings_date,
         'ticker': stock,
         'url': url})

    summary_data.update(price_data)
    summary_data.update(summary_detail_data)
    summary_data.update(recommendation_trend_data)

    utils.del_none_values_in_json(summary_data)
    return summary_data


def parse_cash_flow_statement(json_raw_result, ticker):
    cash_flow_statements_list = json_raw_result["cashflowStatementHistory"]["cashflowStatements"]
    cash_flow_statement_data = []
    for cash_flow_statement_yearly in cash_flow_statements_list:
        cash_flow = utils.raw_json_answer_parser(cash_flow_statement_yearly)
        cash_flow['ticker'] = ticker
        cash_flow_statement_data.append(cash_flow)
    return cash_flow_statement_data


def parse_income_statement(json_raw_result, ticker):
    income_statement_history_list = json_raw_result["incomeStatementHistory"]["incomeStatementHistory"]
    income_statement_data = []

    for income_statement_history in income_statement_history_list:
        income_statement = utils.raw_json_answer_parser(income_statement_history)
        income_statement['ticker'] = ticker
        income_statement_data.append(income_statement)

    return income_statement_data
