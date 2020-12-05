#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso/list-account-roles.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # access-token : The token issued by the CreateToken API call. For more information, see CreateToken in the AWS SSO OIDC API Reference Guide .
    # account-id : The identifier for the AWS account that is assigned to the user.
    """

    execute_two_parameter("sso", "list-account-roles", "access-token", "account-id", parameter_display_string)