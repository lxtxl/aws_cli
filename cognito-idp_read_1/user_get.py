#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-user.html
if __name__ == '__main__':
    """
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-users.html
    """

    parameter_display_string = """
    # access-token : The access token returned by the server response to get information about the user.
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

    execute_one_parameter("cognito-idp", "get-user", "access-token", add_option_dict)