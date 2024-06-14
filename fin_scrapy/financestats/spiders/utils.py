# coding=utf-8

from collections import OrderedDict

def del_none_values_in_json(json_obj):
    """
    Delete keys with the value ``None`` in a dictionary, recursively.

    This alters the input so you may wish to ``copy`` the dict first.
    """
    # For Python 3, write `list(d.items())`; `d.items()` won’t work
    # For Python 2, write `d.items()`; `d.iteritems()` won’t work
    for key, value in list(json_obj.items()):
        if "." in key:
            new_key = key.replace(".", "")
            json_obj[new_key] = json_obj.pop(key)
        if value is None:
            print(("This value is None : %s " % value))
            del json_obj[key]
        elif isinstance(value, dict):
            del_none_values_in_json(value)
        elif isinstance(value, set):
            json_obj[key].discard(None)
            try:
                json_obj[key] = json_obj[key].pop()
            except:
                pass
    return json_obj  # For convenience


def raw_json_answer_parser(price_dict_raw):
    price_data = {}
    for key, value in list(price_dict_raw.items()):
        if type(value) is dict:
            if len(value) == 0 or len(value) == 1:
                continue
            if "date" in key:
                print(key)
                print(value)
                price_data[key] = value['fmt']
            else:
                price_data[key] = value['raw']
            continue
        price_data[key] = value
    return price_data


def parse_dom_table(table):
    summary_data = OrderedDict()
    for table_data in table:
        raw_table_key = table_data.xpath('.//td[contains(@class,"C(black)")]//text()').extract_first()
        raw_table_value = table_data.xpath('.//td[contains(@class,"Ta(end)")]//text()').extract_first()
        table_key = ''.join(raw_table_key).strip()
        table_value = ''.join(raw_table_value).strip()
        summary_data.update({table_key: table_value})
    return summary_data
