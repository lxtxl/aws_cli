#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/verify-user-attribute.html
if __name__ == '__main__':
    """
	delete-user-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user-attributes.html
	update-user-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-attributes.html
    """

    parameter_display_string = """
    # access-token : Represents the access token of the request to verify user attributes.
    # attribute-name : The attribute name in the request to verify user attributes.
    # code : The verification code in the request to verify user attributes.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cognito-idp", "verify-user-attribute", "access-token", "attribute-name", "code", add_option_dict)
