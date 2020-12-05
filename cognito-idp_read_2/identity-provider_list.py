#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-identity-provider.html
if __name__ == '__main__':
    """
	create-identity-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-identity-provider.html
	delete-identity-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-identity-provider.html
	list-identity-providers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-identity-providers.html
	update-identity-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-identity-provider.html
    """

    parameter_display_string = """
    # user-pool-id : The user pool ID.
    # provider-name : The identity provider name.
    """

    execute_two_parameter("cognito-idp", "describe-identity-provider", "user-pool-id", "provider-name", parameter_display_string)