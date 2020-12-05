#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/forgot-password.html
if __name__ == '__main__':
    """
	change-password : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/change-password.html
    """

    parameter_display_string = """
    # client-id : The ID of the client associated with the user pool.
    # username : The user name of the user for whom you want to enter a code to reset a forgotten password.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cognito-idp", "forgot-password", "client-id", "username", add_option_dict)
