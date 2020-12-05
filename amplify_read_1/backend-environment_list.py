#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-backend-environments.html
if __name__ == '__main__':
    """
	create-backend-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/create-backend-environment.html
	delete-backend-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-backend-environment.html
	get-backend-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/get-backend-environment.html
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

    execute_one_parameter("amplify", "list-backend-environments", "app-id", add_option_dict)