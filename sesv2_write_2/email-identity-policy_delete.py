#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-email-identity-policy.html
if __name__ == '__main__':
    """
	create-email-identity-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-email-identity-policy.html
	get-email-identity-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-email-identity-policies.html
	update-email-identity-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/update-email-identity-policy.html
    """

    parameter_display_string = """
    # email-identity : The email identity for which you want to delete a policy.
    # policy-name : The name of the policy.
The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sesv2", "delete-email-identity-policy", "email-identity", "policy-name", add_option_dict)
