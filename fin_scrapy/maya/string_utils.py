import re

def is_year_by_regex(string):
    regex_pattern = "(19|20)\d{2}"
    result = re.match(regex_pattern, string)
    return result

def remove_empty_key_value_from_dictionary(dictionary_of_strings):
    new_dictionary = {}
    regex = re.compile(r'[\(*\)\n\r\t]')
    for elem in list(dictionary_of_strings.keys()):
        key = regex.sub("", elem)
        value = regex.sub("", dictionary_of_strings[elem])
        if key != None and bool(value.strip()) == True:
            new_dictionary[key] = value
    return new_dictionary


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
