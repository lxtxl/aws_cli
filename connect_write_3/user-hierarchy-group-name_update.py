#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-user-hierarchy-group-name.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # name : The name of the hierarchy group. Must not be more than 100 characters.
    # hierarchy-group-id : The identifier of the hierarchy group.
    # instance-id : The identifier of the Amazon Connect instance.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("connect", "update-user-hierarchy-group-name", "name", "hierarchy-group-id", "instance-id", add_option_dict)
