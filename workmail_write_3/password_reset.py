#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/reset-password.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # organization-id : The identifier of the organization that contains the user for which the password is reset.
    # user-id : The identifier of the user for whom the password is reset.
    # password : The new password for the user.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("workmail", "reset-password", "organization-id", "user-id", "password", add_option_dict)
