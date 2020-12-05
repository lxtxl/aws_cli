#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/remove-resource-permission.html
if __name__ == '__main__':
    """
	add-resource-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/add-resource-permissions.html
	describe-resource-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-resource-permissions.html
    """

    parameter_display_string = """
    # resource-id : The ID of the resource.
    # principal-id : The principal ID of the resource.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workdocs", "remove-resource-permission", "resource-id", "principal-id", add_option_dict)
