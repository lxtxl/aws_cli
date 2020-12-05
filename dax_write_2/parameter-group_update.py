#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/update-parameter-group.html
if __name__ == '__main__':
    """
	create-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/create-parameter-group.html
	delete-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/delete-parameter-group.html
	describe-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/describe-parameter-groups.html
    """

    parameter_display_string = """
    # parameter-group-name : The name of the parameter group.
    # parameter-name-values : An array of name-value pairs for the parameters in the group. Each element in the array represents a single parameter.
(structure)

An individual DAX parameter.
ParameterName -> (string)

The name of the parameter.

ParameterValue -> (string)

The value of the parameter.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dax", "update-parameter-group", "parameter-group-name", "parameter-name-values", add_option_dict)
