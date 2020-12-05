#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-resource-servers.html
if __name__ == '__main__':
    """
	create-resource-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-resource-server.html
	delete-resource-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-resource-server.html
	describe-resource-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-resource-server.html
	update-resource-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-resource-server.html
    """

    parameter_display_string = """
    # user-pool-id : The user pool ID for the user pool.
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

    execute_one_parameter("cognito-idp", "list-resource-servers", "user-pool-id", add_option_dict)