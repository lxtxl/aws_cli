#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/set-identity-pool-configuration.html
if __name__ == '__main__':
    """
	get-identity-pool-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/get-identity-pool-configuration.html
    """

    parameter_display_string = """
    # identity-pool-id : A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool to modify.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cognito-sync", "set-identity-pool-configuration", "identity-pool-id", add_option_dict)





