#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/set-identity-pool-roles.html
if __name__ == '__main__':
    """
	get-identity-pool-roles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/get-identity-pool-roles.html
    """

    parameter_display_string = """
    # identity-pool-id : An identity pool ID in the format REGION:GUID.
    # roles : The map of roles associated with this pool. For a given role, the key will be either âauthenticatedâ or âunauthenticatedâ and the value will be the Role ARN.
key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cognito-identity", "set-identity-pool-roles", "identity-pool-id", "roles", add_option_dict)
