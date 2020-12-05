#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/list-identity-policies.html
if __name__ == '__main__':
    """
	delete-identity-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-identity-policy.html
	get-identity-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-identity-policies.html
	put-identity-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/put-identity-policy.html
    """

    parameter_display_string = """
    # identity : The identity that is associated with the policy for which the policies will be listed. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com , example.com , arn:aws:ses:us-east-1:123456789012:identity/example.com .
To successfully call this API, you must own the identity.
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

    execute_one_parameter("ses", "list-identity-policies", "identity", add_option_dict)