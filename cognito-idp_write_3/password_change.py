#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/change-password.html
if __name__ == '__main__':
    """
	forgot-password : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/forgot-password.html
    """

    parameter_display_string = """
    # previous-password : The old password.
    # proposed-password : The new password.
    # access-token : The access token.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cognito-idp", "change-password", "previous-password", "proposed-password", "access-token", add_option_dict)
