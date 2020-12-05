#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/delete-identity-pool.html
if __name__ == '__main__':
    """
	create-identity-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/create-identity-pool.html
	describe-identity-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/describe-identity-pool.html
	list-identity-pools : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/list-identity-pools.html
	update-identity-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/update-identity-pool.html
    """

    parameter_display_string = """
    # identity-pool-id : An identity pool ID in the format REGION:GUID.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cognito-identity", "delete-identity-pool", "identity-pool-id", add_option_dict)





