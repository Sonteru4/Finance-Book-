import json
from json import JSONEncoder


class FileEntry(object):
    def __init__(self, file_name, bspage, ispage, cfpage, year, cpa):
        self.file_name = file_name
        self.bspage = bspage
        self.ispage = ispage
        self.cpa = cpa
        self.year = year
        self.cfpage = cfpage


class CompanyDetails(object):
    def __init__(self, company_name, maya_id, tckr):
        self.company_name = company_name
        self.maya_id = maya_id
        self.tcker = tckr
        self.data = []


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def get_input(message):
    input_message = raw_input(message + " \r\n")
    if "end" in input_message.lower():
        return None
    return input_message


def main():
    print "Hello, when you want to exit enter 'end'"
    companies = []
    while True:
        message = get_input("Enter company name - if you want to end enter 'end'")
        if None == message:
            print "go out \r\n"
            break
        maya_id = get_input("Enter maya id ")
        tckr = get_input("enter tckr")
        c = CompanyDetails(message, maya_id, tckr)

        while True:
            file_name = get_input("Enter new file name - PDF NAME - Enter 'end' if you want to end")
            bspage = get_input("Enter bspage")
            ispage = get_input("Enter ispage")
            cfpage = get_input("Enter cfpage")
            year = get_input("Enter year")
            cpa = get_input("Enter cpa")
            f = FileEntry(file_name, bspage, ispage, cfpage, year, cpa)
            c.data.append(f)
            if None == get_input("if do you want to move to next company 'ENTER - end', if not just enter"):
                break
        companies.append(c)

        to_save = json.dumps(companies, ensure_ascii=False, cls=MyEncoder, encoding='utf8')
        with open('out.json', 'wb') as f:
            f.write(to_save.encode('utf-8'))


if __name__ == '__main__':
    main()
