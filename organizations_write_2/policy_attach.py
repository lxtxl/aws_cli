#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/attach-policy.html
if __name__ == '__main__':
    """
	create-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-policy.html
	delete-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-policy.html
	describe-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-policy.html
	detach-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/detach-policy.html
	list-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-policies.html
	update-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/update-policy.html
    """

    parameter_display_string = """
    # policy-id : The unique identifier (ID) of the policy that you want to attach to the target. You can get the ID for the policy by calling the  ListPolicies operation.
The regex pattern for a policy ID string requires âp-â followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).
    # target-id : The unique identifier (ID) of the root, OU, or account that you want to attach the policy to. You can get the ID by calling the  ListRoots ,  ListOrganizationalUnitsForParent , or  ListAccounts operations.
The regex pattern for a target ID string requires one of the following:

Root - A string that begins with âr-â followed by from 4 to 32 lowercase letters or digits.
Account - A string that consists of exactly 12 digits.
Organizational unit (OU) - A string that begins with âou-â followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second â-â dash and from 8 to 32 additional lowercase letters or digits.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("organizations", "attach-policy", "policy-id", "target-id", add_option_dict)
