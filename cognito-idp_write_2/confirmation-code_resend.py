#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/resend-confirmation-code.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # client-id : The ID of the client associated with the user pool.
    # username : The user name of the user to whom you wish to resend a confirmation code.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cognito-idp", "resend-confirmation-code", "client-id", "username", add_option_dict)
