#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/delete-user.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-user.html
	describe-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-users.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # user-id : The identifier of the user.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("connect", "delete-user", "instance-id", "user-id", add_option_dict)
