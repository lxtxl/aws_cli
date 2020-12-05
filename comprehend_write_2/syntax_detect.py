#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/detect-syntax.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # text : A UTF-8 string. Each string must contain fewer that 5,000 bytes of UTF encoded characters.
    # language-code : The language code of the input documents. You can specify any of the following languages supported by Amazon Comprehend: German (âdeâ), English (âenâ), Spanish (âesâ), French (âfrâ), Italian (âitâ), or Portuguese (âptâ).
Possible values:

en
es
fr
de
it
pt
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("comprehend", "detect-syntax", "text", "language-code", add_option_dict)
