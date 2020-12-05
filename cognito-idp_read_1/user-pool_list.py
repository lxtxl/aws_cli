#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-user-pool.html
if __name__ == '__main__':
    """
	create-user-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-pool.html
	delete-user-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user-pool.html
	list-user-pools : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-user-pools.html
	update-user-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-pool.html
    """

    parameter_display_string = """
    # user-pool-id : The user pool ID for the user pool you want to describe.
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

    execute_one_parameter("cognito-idp", "describe-user-pool", "user-pool-id", add_option_dict)