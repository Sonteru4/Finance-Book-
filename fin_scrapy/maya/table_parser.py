import json
from string_utils import *
import xlsxwriter

class ValueIndexPair:
    def __init__(self, value, index):
        self.index = index
        self.value = value

    @staticmethod
    def sortByValue(obj):
        return int(obj.value)


class KnownWords:
    def __init__(self):
        self.ANNOTATION = ['\u05e8\u05d5\u05d0\u05d1', '\u05e8\u05d5\u05d0\u05d9\u05d1']
        self.TITLE = '\u05e9\u05d7"  \u05d9\u05e4\u05dc\u05d0\u05d1'


class JsonTableParser:
    def __init__(self, file_path, encoding='utf8'):
        with open(file_path) as file:
            self.raw_data = json.load(file, encoding=encoding)
            self.escaped_data = []
            self.years = {}
            self.known_words = KnownWords()

    def parse(self):
        for entry in self.raw_data:
            new_entry = remove_empty_key_value_from_dictionary(entry)
            self.merge_divided_entries(new_entry)
            self.escaped_data.append(new_entry)
            for key, value in list(new_entry.items()):
                new_value = self.parse_years_colunm_from_table(key, value)
                if new_value is not None:
                    new_entry[key] = new_value

        self.add_title_index_if_not_exist()

        self.merge_title_and_numbers_if_divided()
        self.append_data()

    def merge_divided_entries(self, dictionary_of_strings):
        pos = 0
        values = list(dictionary_of_strings.values())
        for elem in list(dictionary_of_strings.keys()):
            pos += 1
            if dictionary_of_strings[elem].endswith(",") or dictionary_of_strings[elem].endswith('\\'):
                dictionary_of_strings[pos] = dictionary_of_strings[elem].replace(',', '') + \
                                             values[pos]
                del dictionary_of_strings[elem]

    def merge_title_and_numbers_if_divided(self):
        pos = 0
        title_pos = self.years["Title"]
        for i in self.escaped_data:
            pos += 1
            keys = list(i.keys())
            if len(keys) == 1 and title_pos in keys and self.escaped_data[pos].get(title_pos, None) == None:
                self.escaped_data[pos][title_pos] = i[title_pos]
                del self.escaped_data[pos - 1]


    def add_title_index_if_not_exist(self):
        if "Title" not in self.years:
            bigger_number = 0
            for i in list(self.years.values()):
                if bigger_number < int(i):
                    bigger_number = int(i)

            index = (bigger_number + 1)
            last_index = int(list(self.escaped_data[-1].keys())[-1])
            if int(last_index) > index:
                self.years["Title"] = str(last_index)
            else:
                self.years["Title"] = str(index)

    def append_data(self):
        new_data = []
        for entry in self.escaped_data:
            new_entry = {}
            try:
                for k, v in self.years.items():
                    new_entry[v] = entry.get(v, "")
            except Exception as e:
                print(e)
            if len(new_entry) != 0:
                new_data.append(new_entry)
        self.escaped_data = new_data

    def parse_years_colunm_from_table(self, index, value):
        is_it_year_entry = False
        try:
            value = ''.join(value)
            year_to_index = self.find_index_and_year(index, value)
            is_it_year_entry = True
            self.years[year_to_index.value] = year_to_index.index
            return value
        except Exception as error:
            print(error)
            if self.known_words.TITLE == value or (is_it_year_entry and not value):
                self.years["Title"] = index
                del self.escaped_data[-1]
            if value in self.known_words.ANNOTATION:
                self.years["Annotation"] = index
        return None

    def find_index_and_year(self, key, value):
        result = is_year_by_regex(value)
        if result:
            return ValueIndexPair(value, key)
        else:
            raise Exception("Cant find regex pattern in string : %s. key : key" % (value, key))


class XlsxWriter():
    def __init__(self, json_table_object):
        self.json_table_object = json_table_object
        self.columns = []
        self.rows = []

    def create_columns_and_rows(self):
        years = self.json_table_object.years

        if "Title" in years:
            self.columns.append("Title")

        list_of_years = list(years.keys())
        only_years = []
        for x in list_of_years:
            if is_year_by_regex(x):
                only_years.append(str(x))

        only_years.sort(key=int)

        for x in only_years:
            self.columns.append(str(x))

        if "Annotation" in years:
            self.columns.append("Annotation")

        for dict_data in self.json_table_object.escaped_data:
            data = []
            for i in self.columns:
                index = years[i]
                try:
                    data.append(str(dict_data[index]))
                except Exception as e:
                    print(e)
            self.rows.append(data)

    def write_to_file(self, path):
        workbook = xlsxwriter.Workbook(path + ".xlsx")
        worksheet = workbook.add_worksheet()
        start_number = 0;
        worksheet.write_row(start_number, 0, data=self.columns)
        for s in self.rows:
            start_number += 1
            s[0] = (s[0])[::-1]
            s[1::] = self.convet_list_of_strings_to_int(s[1::])
            worksheet.write_row(start_number, 0, data=s)
        workbook.close()

    def convet_list_of_strings_to_int(self, lst):
        new_lst = []
        for i in lst:
            try:
                new_lst.append(int(i.replace(',', '')))
            except Exception as e:
                new_lst.append(i)
                print(e)
        return new_lst

        # print (df)
