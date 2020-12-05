#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/batch-detect-entities.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # text-list : A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document must contain fewer than 5,000 bytes of UTF-8 encoded characters.
(string)
    # language-code : The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. All documents must be in the same language.
Possible values:

en
es
fr
de
it
pt
ar
hi
ja
ko
zh
zh-TW
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("comprehend", "batch-detect-entities", "text-list", "language-code", add_option_dict)
