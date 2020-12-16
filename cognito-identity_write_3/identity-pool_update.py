#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/update-identity-pool.html
if __name__ == '__main__':
    """
	create-identity-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/create-identity-pool.html
	delete-identity-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/delete-identity-pool.html
	describe-identity-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/describe-identity-pool.html
	list-identity-pools : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/list-identity-pools.html
    """

    parameter_display_string = """
    # identity-pool-id : An identity pool ID in the format REGION:GUID.
    # identity-pool-name : A string that you provide.
    # allow-unauthenticated-identities | --no-allow-unauthenticated-identities : TRUE if the identity pool supports unauthenticated logins.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cognito-identity", "update-identity-pool", "identity-pool-id", "identity-pool-name", "allow-unauthenticated-identities | --no-allow-unauthenticated-identities", add_option_dict)
