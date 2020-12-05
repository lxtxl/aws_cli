#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/respond-to-auth-challenge.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # client-id : The app client ID.
    # challenge-name : The challenge name. For more information, see InitiateAuth .

ADMIN_NO_SRP_AUTH is not a valid value.

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
    write_two_parameter("cognito-idp", "respond-to-auth-challenge", "client-id", "challenge-name", add_option_dict)
