#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/lookup-developer-identity.html
if __name__ == '__main__':
    """
	merge-developer-identities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/merge-developer-identities.html
	unlink-developer-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/unlink-developer-identity.html
    """

    parameter_display_string = """
    # identity-pool-id : An identity pool ID in the format REGION:GUID.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cognito-identity", "lookup-developer-identity", "identity-pool-id", add_option_dict)





