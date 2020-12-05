#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/remove-attributes-from-findings.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # finding-arns : The ARNs that specify the findings that you want to remove attributes from.
(string)
    # attribute-keys : The array of attribute keys that you want to remove from specified findings.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("inspector", "remove-attributes-from-findings", "finding-arns", "attribute-keys", add_option_dict)
