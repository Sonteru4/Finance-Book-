import os
from collections import OrderedDict

import requests
import xlrd

from fin_scrapy.utils.mongohandler import *

DAMODARN_URL = "http://www.stern.nyu.edu/~adamodar/pc/datasets/"
BETAS = "betas.xls"
MONGO_ADDRESS = 'mongodb://localhost:27017/'
MONGO_CONNECTION = Mongo_Client_Wrapper(MONGO_ADDRESS)
COUNTRYֹֹּ_PREMIUM = "ctryprem.xls"


def get_titles_row(title, row_values):
    is_row = False
    titles = []
    for val in row_values:
        titles.append(val)
        if title == val:
            is_row = True

    if is_row == False:
        titles = None
    return titles


def parse_damodarn_data_set(file_path, title_to_parse, sheet):
    # Open the workbook and select the first worksheet
    wb = xlrd.open_workbook(file_path)
    sh = wb.sheet_by_name(sheet)
    # List to hold dictionaries
    industry_data = []
    keys = []
    started_row = 0
    # Iterate through each row in worksheet and fetch values into dict
    for rownum in range(1, sh.nrows):

        row_values = sh.row_values(rownum)
        titles = get_titles_row(title_to_parse, row_values)
        if titles is not None:
            keys = titles
            started_row = rownum + 1
            break

    for rownum in range(started_row, sh.nrows):
        data = OrderedDict()
        index = 0
        row_values = sh.row_values(rownum)
        for t in keys:
            data[t] = row_values[index]
            index += 1
        industry_data.append(data)

    return industry_data


def write_data_to_file(temp_file_name, buffer):
    with open(temp_file_name, "wb") as f:
        f.write(buffer)


def insert_dict_to_database(data):
    for industry in data:
        MONGO_CONNECTION.mongo_insert("damodarn", industry)


def download_damodarn_dataset(file_name_from_server, first_row_title, sheet_name):
    request = requests.get(DAMODARN_URL + file_name_from_server)
    temp_file_name = '{}'.format(hash(os.times()))
    if request.status_code == 200:
        write_data_to_file(temp_file_name, request.content)
        data = parse_damodarn_data_set(temp_file_name, first_row_title, sheet_name)
        os.remove(temp_file_name)
        insert_dict_to_database(data)


def download_all_data_from_damodarn():
    download_damodarn_dataset(BETAS, "Industry Name", "Sheet1")
    download_damodarn_dataset(COUNTRYֹֹּ_PREMIUM, "Country", "ERPs by country")


if __name__ == '__main__':
    download_all_data_from_damodarn()
