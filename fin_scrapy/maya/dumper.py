#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import argparse
import os
import sys
import camelot
from file_system_watcher import *


def create_json_file_from_pdf(pdf_path, file_start_with, page_number, flavor='stream'):
    watcher = FileSystemWatcher(os.getcwd(), file_start_with)
    try:
        tables = camelot.read_pdf(pdf_path, pages=page_number, flavor=flavor)
        tables.export(file_start_with, f='json')

    except Exception as e:
        print(e)
    return watcher.get_diff()


class Dumper:
    DATA_PATH = "data"
    JSON_NOT_VALID_VALUE = "q"

    def __init__(self, instructions_file_path):
        self.instructions_json = deserialize_json(cls=CompanyDetails, sub_cls=FileEntry, path=instructions_file_path)
        self.pdf_page_dict = {}

    def deserialize_json(self, cls=None, sub_cls=None, path=None):
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

    def get_list_instructions(self):

        for instruction in self.instructions_json:
            folder_by_id = instruction.mayaid
            for location in instruction.list:
                try:
                    if JSON_NOT_VALID_VALUE not in location.pdf:
                        pdf_name = location.pdf + ".pdf"
                        full_path = os.path.join(os.getcwd(), "../" + self.DATA_PATH, folder_by_id, pdf_name)

                        self.pdf_page_dict[full_path] = location.bspage
                except Exception as e:
                    print(e)

    def parse(self):
        for pdf_path, page in self.pdf_page_dict.items():
            try:
                head, tail = os.path.split(pdf_path)
                file_start_with = ("json-%s" % tail.split(".")[0])
                files = create_json_file_from_pdf(path, file_start_with, page)
                move_files_to_output_directory(files, output_directory)
            except Exception as e:
                print(e)

        print("file : %s, pdf : %s" % (files, path))


class StoreDictKeyPair(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        self._nargs = nargs
        super(StoreDictKeyPair, self).__init__(option_strings, dest, nargs=nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        my_dict = {}
        # print "values: {}".format(values)
        for kv in values:
            k, v = kv.split("=")
            my_dict[k] = v
        setattr(namespace, self.dest, my_dict)


if __name__ == '__main__':
    print("current direcory %s" % sys.path)
    parser = argparse.ArgumentParser(description='Dump table from page in a pdf to json file')
    parser.add_argument("-key_pairs", dest="my_dict", action=StoreDictKeyPair, nargs="+", metavar="KEY=VAL",
                        help='example : pdf_path1=page, pdf_path2=page ...')
    parser.add_argument("-output_dir", dest="output_directory", type=str,
                        help='Output directory to write files')

    args = parser.parse_args(sys.argv[1:])
    print("start to parse : %s \r\n" % args)
    main(args.my_dict, args.output_directory)
