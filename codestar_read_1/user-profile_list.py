#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/describe-user-profile.html
if __name__ == '__main__':
    """
	create-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/create-user-profile.html
	delete-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/delete-user-profile.html
	list-user-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/list-user-profiles.html
	update-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/update-user-profile.html
    """

    parameter_display_string = """
    # user-arn : The Amazon Resource Name (ARN) of the user.
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

    execute_one_parameter("codestar", "describe-user-profile", "user-arn", add_option_dict)