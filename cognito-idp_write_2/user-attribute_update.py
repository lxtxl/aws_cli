#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-attributes.html
if __name__ == '__main__':
    """
	delete-user-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user-attributes.html
	verify-user-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/verify-user-attribute.html
    """

    parameter_display_string = """
    # user-attributes : An array of name-value pairs representing user attributes.
For custom attributes, you must prepend the custom: prefix to the attribute name.
(structure)

Specifies whether the attribute is standard or custom.
Name -> (string)

The name of the attribute.

Value -> (string)

The value of the attribute.
    # access-token : The access token for the request to update user attributes.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cognito-idp", "update-user-attributes", "user-attributes", "access-token", add_option_dict)
