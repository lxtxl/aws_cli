#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-respond-to-auth-challenge.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # user-pool-id : The ID of the Amazon Cognito user pool.
    # client-id : The app client ID.
    # challenge-name : The challenge name. For more information, see AdminInitiateAuth .
Possible values:

SMS_MFA
SOFTWARE_TOKEN_MFA
SELECT_MFA_TYPE
MFA_SETUP
PASSWORD_VERIFIER
CUSTOM_CHALLENGE
DEVICE_SRP_AUTH
DEVICE_PASSWORD_VERIFIER
ADMIN_NO_SRP_AUTH
NEW_PASSWORD_REQUIRED
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cognito-idp", "admin-respond-to-auth-challenge", "user-pool-id", "client-id", "challenge-name", add_option_dict)
