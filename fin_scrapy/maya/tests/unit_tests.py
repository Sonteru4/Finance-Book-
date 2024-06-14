import datetime
import json
import os
import random
import shutil
import subprocess
import sys
import unittest
from maya import dumper

sys.path.append("../")
from table_parser import *

from bson.objectid import ObjectId


class FileEntry(object):
    def __init__(self, pdf, bspage, ispage, cfpage, year, cpa, q):
        self.pdf = pdf
        self.bspage = bspage
        self.ispage = ispage
        self.cpa = cpa
        self.year = year
        self.cfpage = cfpage
        self.q = q


class CompanyDetails(object):
    def __init__(self, company_name, maya_id, tckr):
        self.company_name = company_name
        self.maya_id = maya_id
        self.tcker = tckr
        self.list = []


def deserialize_json(cls=None, sub_cls=None, path=None):
    def read_json(_path):
        with open(_path, "r", encoding="utf8") as file:
            return json.load(file)

    companies = read_json(path)

    l = []
    for company in companies:
        instance = object.__new__(cls)
        for key, value in list(company.items()):
            if isinstance(value, list):
                o = []
                for row in value:
                    sub_instance = object.__new__(sub_cls)
                    for k, v in list(row.items()):
                        setattr(sub_instance, k, v)
                    o.append(sub_instance)
                setattr(instance, key, o)
            else:
                setattr(instance, key, value)
        l.append(instance)

    return l


class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return o.__dict__


class DumperTests(unittest.TestCase):
    def get_random_int(self, min=0, max=sys.maxsize):
        return random.randint(min, max)

    def test_dumper(self):
        sys.path.append("../")
        dir = "pdf_examples"
        list_dir = os.listdir(dir)
        file_page_dict = {"example.pdf": 60, "KPMG2.pdf": 58, "KPMG3.pdf": 399, "NOTKPMG.pdf": 84}
        key_value = []
        for file in list_dir:
            head, tail = os.path.split(file)
            formated_string = os.path.join(dir, file) + "=" + str(file_page_dict[tail]) + " "
            key_value.append(formated_string)

        pdf_params = "".join(key_value)
        output_dir = "out"
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        process_command = "pythonw ../dumper.py -output_dir %s -key_pairs %s" % (output_dir, pdf_params)
        subprocess.call(process_command, shell=True)

        files = os.listdir(output_dir)
        self.assertEqual(len(files), len(file_page_dict), "Number of files doesnt appropriate to number of pdfs")
        for file in files:
            self.assertGreater(os.stat(os.path.join(output_dir, file)).st_size, 0, ("the file didnt parsed %s", file))

    @staticmethod
    def test_all_current_data():
        try:
            sys.path.append("../")
            file_path = "../data/convert.json"
            json_object = deserialize_json(cls=CompanyDetails, sub_cls=FileEntry, path=file_path)
            path = "data"
            key_value = []
            for i in json_object:
                folder = i.mayaid
                for x in i.list:
                    try:
                        if "q" not in x.pdf:
                            formated_string = os.path.join(os.getcwd(), "../" + path, folder,
                                                           x.pdf + ".pdf") + "=" + str(
                                x.bspage) + " "
                            key_value.append(formated_string)
                    except Exception as e:
                        print(e)

            pdf_params = "".join(key_value)
            print(len(key_value))
            print(pdf_params)
            process_command = "pythonw ../dumper.py -output_dir %s -key_pairs %s" % ("test_bs2_pages_out", pdf_params)
            subprocess.call(process_command, shell=True)


        except Exception as e:
            print("Failed")
            print(e)
        # list_dir = os.listdir("../data")


class TableParserTests(unittest.TestCase):
    def get_random_int(self, min=0, max=sys.maxsize):
        return random.randint(min, max)

    def test_writer(self):
        sys.path.append("../")
        dir = "test_bs2_pages_out"
        list_dir = os.listdir(dir)
        output_dir = os.path.join(dir, "xslx")
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)

        os.mkdir(output_dir)

        for file in list_dir:
            print("started to parse file : %s" % file)
            try:
                head, tail = os.path.split(file)
                j = JsonTableParser(os.path.join(path, file))
                j.parse()
                c = XlsxWriter(j)
                c.create_columns_and_rows()

                csv_path = os.path.join(output_dir, tail)
                c.write_to_file(csv_path)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    unittest.main()
