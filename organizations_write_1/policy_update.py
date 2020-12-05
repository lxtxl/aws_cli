#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/update-policy.html
if __name__ == '__main__':
    """
	attach-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/attach-policy.html
	create-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-policy.html
	delete-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-policy.html
	describe-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-policy.html
	detach-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/detach-policy.html
	list-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-policies.html
    """

    parameter_display_string = """
    # policy-id : The unique identifier (ID) of the policy that you want to update.
The regex pattern for a policy ID string requires âp-â followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("organizations", "update-policy", "policy-id", add_option_dict)





