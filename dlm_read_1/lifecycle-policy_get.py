#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/get-lifecycle-policy.html
if __name__ == '__main__':
    """
	create-lifecycle-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/create-lifecycle-policy.html
	delete-lifecycle-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/delete-lifecycle-policy.html
	get-lifecycle-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/get-lifecycle-policies.html
	update-lifecycle-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/update-lifecycle-policy.html
    """

    parameter_display_string = """
    # policy-id : The identifier of the lifecycle policy.
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

    execute_one_parameter("dlm", "get-lifecycle-policy", "policy-id", add_option_dict)