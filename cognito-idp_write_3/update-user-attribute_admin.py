#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-update-user-attributes.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # user-pool-id : The user pool ID for the user pool where you want to update user attributes.
    # username : The user name of the user for whom you want to update user attributes.
    # user-attributes : An array of name-value pairs representing user attributes.
For custom attributes, you must prepend the custom: prefix to the attribute name.
(structure)

Specifies whether the attribute is standard or custom.
Name -> (string)

The name of the attribute.

Value -> (string)

The value of the attribute.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cognito-idp", "admin-update-user-attributes", "user-pool-id", "username", "user-attributes", add_option_dict)
