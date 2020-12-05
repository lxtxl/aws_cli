#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user-attributes.html
if __name__ == '__main__':
    """
	update-user-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-attributes.html
	verify-user-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/verify-user-attribute.html
    """

    parameter_display_string = """
    # user-attribute-names : An array of strings representing the user attribute names you wish to delete.
For custom attributes, you must prepend the custom: prefix to the attribute name.
(string)
    # access-token : The access token used in the request to delete user attributes.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cognito-idp", "delete-user-attributes", "user-attribute-names", "access-token", add_option_dict)
