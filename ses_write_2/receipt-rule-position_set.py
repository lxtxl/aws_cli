#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/set-receipt-rule-position.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # rule-set-name : The name of the receipt rule set that contains the receipt rule to reposition.
    # rule-name : The name of the receipt rule to reposition.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ses", "set-receipt-rule-position", "rule-set-name", "rule-name", add_option_dict)
