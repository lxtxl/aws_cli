#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/confirm-sign-up.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # client-id : The ID of the app client associated with the user pool.
    # username : The user name of the user whose registration you wish to confirm.
    # confirmation-code : The confirmation code sent by a userâs request to confirm registration.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cognito-idp", "confirm-sign-up", "client-id", "username", "confirmation-code", add_option_dict)
