#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-routing-profile-name.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # routing-profile-id : The identifier of the routing profile.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("connect", "update-routing-profile-name", "instance-id", "routing-profile-id", add_option_dict)
