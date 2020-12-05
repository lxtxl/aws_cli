#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-identity-policies.html
if __name__ == '__main__':
    """
	delete-identity-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-identity-policy.html
	list-identity-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/list-identity-policies.html
	put-identity-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/put-identity-policy.html
    """

    parameter_display_string = """
    # identity : The identity for which the policies will be retrieved. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com , example.com , arn:aws:ses:us-east-1:123456789012:identity/example.com .
To successfully call this API, you must own the identity.
    # policy-names : A list of the names of policies to be retrieved. You can retrieve a maximum of 20 policies at a time. If you do not know the names of the policies that are attached to the identity, you can use ListIdentityPolicies .
(string)
    """

    execute_two_parameter("ses", "get-identity-policies", "identity", "policy-names", parameter_display_string)