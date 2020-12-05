#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-policy.html
if __name__ == '__main__':
    """
	attach-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/attach-policy.html
	create-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-policy.html
	delete-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-policy.html
	detach-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/detach-policy.html
	list-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-policies.html
	update-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/update-policy.html
    """

    parameter_display_string = """
    # policy-id : The unique identifier (ID) of the policy that you want details about. You can get the ID from the  ListPolicies or  ListPoliciesForTarget operations.
The regex pattern for a policy ID string requires âp-â followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).
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

    execute_one_parameter("organizations", "describe-policy", "policy-id", add_option_dict)