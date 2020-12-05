#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-webhooks.html
if __name__ == '__main__':
    """
	create-webhook : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/create-webhook.html
	delete-webhook : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-webhook.html
	get-webhook : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/get-webhook.html
	update-webhook : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/update-webhook.html
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

    execute_one_parameter("amplify", "list-webhooks", "app-id", add_option_dict)