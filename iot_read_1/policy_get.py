#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-policy.html
if __name__ == '__main__':
    """
	attach-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-policy.html
	create-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-policy.html
	delete-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-policy.html
	detach-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/detach-policy.html
	list-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-policies.html
    """

    parameter_display_string = """
    # policy-name : The name of the policy.
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

    execute_one_parameter("iot", "get-policy", "policy-name", add_option_dict)