#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/get-identity-pool-roles.html
if __name__ == '__main__':
    """
	set-identity-pool-roles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/set-identity-pool-roles.html
    """

    parameter_display_string = """
    # identity-pool-id : An identity pool ID in the format REGION:GUID.
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

    execute_one_parameter("cognito-identity", "get-identity-pool-roles", "identity-pool-id", add_option_dict)