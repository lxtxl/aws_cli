#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-termination-protection.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # enable-termination-protection | --no-enable-termination-protection : Whether to enable termination protection on the specified stack.
    # stack-name : The name or unique ID of the stack for which you want to set termination protection.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudformation", "update-termination-protection", "enable-termination-protection | --no-enable-termination-protection", "stack-name", add_option_dict)
