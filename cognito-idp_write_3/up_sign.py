#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/sign-up.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # client-id : The ID of the client associated with the user pool.
    # username : The user name of the user you wish to register.
    # password : The password of the user you wish to register.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cognito-idp", "sign-up", "client-id", "username", "password", add_option_dict)
