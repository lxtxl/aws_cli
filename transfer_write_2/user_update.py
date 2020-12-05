#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/update-user.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/create-user.html
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/delete-user.html
	describe-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/list-users.html
    """

    parameter_display_string = """
    # server-id : A system-assigned unique identifier for a server instance that the user account is assigned to.
    # user-name : A unique string that identifies a user and is associated with a server as specified by the ServerId . This user name must be a minimum of 3 and a maximum of 100 characters long. The following are valid characters: a-z, A-Z, 0-9, underscore â_â, hyphen â-â, period â.â, and at sign â@â. The user name canât start with a hyphen, period, or at sign.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("transfer", "update-user", "server-id", "user-name", add_option_dict)
