#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/restore-managed-prefix-list-version.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # prefix-list-id : The ID of the prefix list.
    # previous-version : 
    # current-version : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ec2", "restore-managed-prefix-list-version", "prefix-list-id", "previous-version", "current-version", add_option_dict)
