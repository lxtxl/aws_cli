#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-users.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-user.html
	get-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-user.html
	invite-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/invite-users.html
	logout-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/logout-user.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-user.html
    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("chime", "list-users", "account-id", add_option_dict)