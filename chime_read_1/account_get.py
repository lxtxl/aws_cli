#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-account.html
if __name__ == '__main__':
    """
	create-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-account.html
	delete-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-account.html
	list-accounts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-accounts.html
	update-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-account.html
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

    execute_one_parameter("chime", "get-account", "account-id", add_option_dict)