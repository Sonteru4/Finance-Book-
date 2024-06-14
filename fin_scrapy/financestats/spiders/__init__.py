# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import sys

sys.path.append('../../')

TRACE_FILES = ["parser", "finance", "mongohandler", "utils.py"]

def trace_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    func_line_no = frame.f_lineno
    func_filename = co.co_filename
    caller = frame.f_back
    caller_line_no = caller.f_lineno
    caller_filename = caller.f_code.co_filename

    for file_name in TRACE_FILES:
        if file_name in caller_filename:
            if "lib/python2.7/" not in func_filename:
                print(('Call to %s on line %s of %s from line %s of %s' % \
                       (func_name, func_line_no, func_filename, caller_line_no, caller_filename)))

    return


sys.settrace(trace_calls)
