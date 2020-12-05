#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-branches.html
if __name__ == '__main__':
    """
	create-branch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/create-branch.html
	delete-branch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-branch.html
	get-branch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/get-branch.html
	update-branch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/update-branch.html
    """

    parameter_display_string = """
    # app-id : The unique ID for an Amplify app.
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

    execute_one_parameter("amplify", "list-branches", "app-id", add_option_dict)