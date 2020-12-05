#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/add-resource-permissions.html
if __name__ == '__main__':
    """
	describe-resource-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-resource-permissions.html
	remove-resource-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/remove-resource-permission.html
    """

    parameter_display_string = """
    # resource-id : The ID of the resource.
    # principals : The users, groups, or organization being granted permission.
(structure)

Describes the recipient type and ID, if available.
Id -> (string)

The ID of the recipient.

Type -> (string)

The type of the recipient.

Role -> (string)

The role of the recipient.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workdocs", "add-resource-permissions", "resource-id", "principals", add_option_dict)
