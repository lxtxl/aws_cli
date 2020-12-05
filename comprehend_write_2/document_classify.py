#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/classify-document.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # text : The document text to be analyzed.
    # endpoint-arn : The Amazon Resource Number (ARN) of the endpoint.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("comprehend", "classify-document", "text", "endpoint-arn", add_option_dict)
