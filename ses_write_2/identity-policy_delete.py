#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-identity-policy.html
if __name__ == '__main__':
    """
	get-identity-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-identity-policies.html
	list-identity-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/list-identity-policies.html
	put-identity-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/put-identity-policy.html
    """

    parameter_display_string = """
    # identity : The identity that is associated with the policy that you want to delete. You can specify the identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com , example.com , arn:aws:ses:us-east-1:123456789012:identity/example.com .
To successfully call this API, you must own the identity.
    # policy-name : The name of the policy to be deleted.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ses", "delete-identity-policy", "identity", "policy-name", add_option_dict)
