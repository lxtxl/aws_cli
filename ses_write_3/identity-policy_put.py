#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/put-identity-policy.html
if __name__ == '__main__':
    """
	delete-identity-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-identity-policy.html
	get-identity-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-identity-policies.html
	list-identity-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/list-identity-policies.html
    """

    parameter_display_string = """
    # identity : The identity that the policy will apply to. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com , example.com , arn:aws:ses:us-east-1:123456789012:identity/example.com .
To successfully call this API, you must own the identity.
    # policy-name : The name of the policy.
The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.
    # policy : The text of the policy in JSON format. The policy cannot exceed 4 KB.
For information about the syntax of sending authorization policies, see the Amazon SES Developer Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ses", "put-identity-policy", "identity", "policy-name", "policy", add_option_dict)
