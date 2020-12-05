#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/delete-user.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/create-user.html
	describe-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/list-users.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/update-user.html
    """

    parameter_display_string = """
    # server-id : A system-assigned unique identifier for a server instance that has the user assigned to it.
    # user-name : A unique string that identifies a user that is being deleted from a server.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("transfer", "delete-user", "server-id", "user-name", add_option_dict)
