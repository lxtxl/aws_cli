#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-user-routing-profile.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # routing-profile-id : The identifier of the routing profile for the user.
    # user-id : The identifier of the user account.
    # instance-id : The identifier of the Amazon Connect instance.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("connect", "update-user-routing-profile", "routing-profile-id", "user-id", "instance-id", add_option_dict)
