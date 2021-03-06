#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-login-profile.html
if __name__ == '__main__':
    """
	create-login-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-login-profile.html
	delete-login-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-login-profile.html
	update-login-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-login-profile.html
    """

    parameter_display_string = """
    # user-name : The name of the user whose login profile you want to retrieve.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
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

    execute_one_parameter("iam", "get-login-profile", "user-name", add_option_dict)