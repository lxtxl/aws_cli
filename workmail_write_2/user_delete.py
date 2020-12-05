#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-user.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-user.html
	describe-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-users.html
    """

    parameter_display_string = """
    # organization-id : The organization that contains the user to be deleted.
    # user-id : The identifier of the user to be deleted.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workmail", "delete-user", "organization-id", "user-id", add_option_dict)
