#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-get-user.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # user-pool-id : The user pool ID for the user pool where you want to get information about the user.
    # username : The user name of the user you wish to retrieve.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cognito-idp", "admin-get-user", "user-pool-id", "username", add_option_dict)
