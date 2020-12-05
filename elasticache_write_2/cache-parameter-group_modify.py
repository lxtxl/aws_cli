#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-cache-parameter-group.html
if __name__ == '__main__':
    """
	create-cache-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-cache-parameter-group.html
	delete-cache-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-cache-parameter-group.html
	describe-cache-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-cache-parameter-groups.html
	reset-cache-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/reset-cache-parameter-group.html
    """

    parameter_display_string = """
    # cache-parameter-group-name : The name of the cache parameter group to modify.
    # parameter-name-values : An array of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional. A maximum of 20 parameters may be modified per request.
(structure)

Describes a name-value pair that is used to update the value of a parameter.
ParameterName -> (string)

The name of the parameter.

ParameterValue -> (string)

The value of the parameter.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elasticache", "modify-cache-parameter-group", "cache-parameter-group-name", "parameter-name-values", add_option_dict)
