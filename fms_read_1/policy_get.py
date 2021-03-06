#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-policy.html
if __name__ == '__main__':
    """
	delete-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/delete-policy.html
	list-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/list-policies.html
	put-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/put-policy.html
    """

    parameter_display_string = """
    # policy-id : The ID of the AWS Firewall Manager policy that you want the details for.
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

    execute_one_parameter("fms", "get-policy", "policy-id", add_option_dict)