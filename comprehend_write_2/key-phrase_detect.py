#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/detect-key-phrases.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # text : A UTF-8 text string. Each string must contain fewer that 5,000 bytes of UTF-8 encoded characters.
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
    write_two_parameter("comprehend", "detect-key-phrases", "text", "language-code", add_option_dict)
