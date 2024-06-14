#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

import pandas as pd
from table_parser import *


def main():
    header_file = ""
    list_of_pdfs = []
    for (root, dirs, files) in os.walk("data"):
        for dir in dirs:
            for file in os.listdir(os.path.join(root, dir)):
                if ".pdf" in file:
                    list_of_pdfs.append(os.path.join(root, dir, file))
        for file in files:
            if ".xlsx" in file:
                header_file = os.path.join(root, file)

    data = pd.read_csv(header_file, error_bad_lines=False)
    print(data.head())

if __name__ == '__main__':
    main()
