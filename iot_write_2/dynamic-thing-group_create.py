#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-dynamic-thing-group.html
if __name__ == '__main__':
    """
	delete-dynamic-thing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-dynamic-thing-group.html
	update-dynamic-thing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-dynamic-thing-group.html
    """

    parameter_display_string = """
    # thing-group-name : The dynamic thing group name to create.
    # query-string : The dynamic thing group search query string.
See Query Syntax for information about query string syntax.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "create-dynamic-thing-group", "thing-group-name", "query-string", add_option_dict)
