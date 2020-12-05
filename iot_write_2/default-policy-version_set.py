#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/set-default-policy-version.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # policy-name : The policy name.
    # policy-version-id : The policy version ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "set-default-policy-version", "policy-name", "policy-version-id", add_option_dict)
