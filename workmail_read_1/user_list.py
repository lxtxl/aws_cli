#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-users.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-user.html
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-user.html
	describe-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-user.html
    """

    parameter_display_string = """
    # organization-id : The identifier for the organization under which the users exist.
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

    execute_one_parameter("workmail", "list-users", "organization-id", add_option_dict)