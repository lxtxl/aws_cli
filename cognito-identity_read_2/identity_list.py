#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/list-identities.html
if __name__ == '__main__':
    """
	delete-identities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/delete-identities.html
	describe-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/describe-identity.html
	unlink-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/unlink-identity.html
    """

    parameter_display_string = """
    # identity-pool-id : An identity pool ID in the format REGION:GUID.
    # max-results : The maximum number of identities to return.
    """

    execute_two_parameter("cognito-identity", "list-identities", "identity-pool-id", "max-results", parameter_display_string)