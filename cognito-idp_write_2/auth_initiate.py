#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/initiate-auth.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # auth-flow : The authentication flow for this call to execute. The API action will depend on this value. For example:

REFRESH_TOKEN_AUTH will take in a valid refresh token and return new tokens.
USER_SRP_AUTH will take in USERNAME and SRP_A and return the SRP variables to be used for next challenge execution.
USER_PASSWORD_AUTH will take in USERNAME and PASSWORD and return the next challenge or tokens.

Valid values include:

USER_SRP_AUTH : Authentication flow for the Secure Remote Password (SRP) protocol.
REFRESH_TOKEN_AUTH /REFRESH_TOKEN : Authentication flow for refreshing the access token and ID token by supplying a valid refresh token.
CUSTOM_AUTH : Custom authentication flow.
USER_PASSWORD_AUTH : Non-SRP authentication flow; USERNAME and PASSWORD are passed directly. If a user migration Lambda trigger is set, this flow will invoke the user migration Lambda if the USERNAME is not found in the user pool.
ADMIN_USER_PASSWORD_AUTH : Admin-based user password authentication. This replaces the ADMIN_NO_SRP_AUTH authentication flow. In this flow, Cognito receives the password in the request instead of using the SRP process to verify passwords.


ADMIN_NO_SRP_AUTH is not a valid value.

Possible values:

USER_SRP_AUTH
REFRESH_TOKEN_AUTH
REFRESH_TOKEN
CUSTOM_AUTH
ADMIN_NO_SRP_AUTH
USER_PASSWORD_AUTH
ADMIN_USER_PASSWORD_AUTH
    # client-id : The app client ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cognito-idp", "initiate-auth", "auth-flow", "client-id", add_option_dict)
