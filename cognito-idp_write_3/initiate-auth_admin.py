#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-initiate-auth.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # user-pool-id : The ID of the Amazon Cognito user pool.
    # client-id : The app client ID.
    # auth-flow : The authentication flow for this call to execute. The API action will depend on this value. For example:

REFRESH_TOKEN_AUTH will take in a valid refresh token and return new tokens.
USER_SRP_AUTH will take in USERNAME and SRP_A and return the SRP variables to be used for next challenge execution.
USER_PASSWORD_AUTH will take in USERNAME and PASSWORD and return the next challenge or tokens.

Valid values include:

USER_SRP_AUTH : Authentication flow for the Secure Remote Password (SRP) protocol.
REFRESH_TOKEN_AUTH /REFRESH_TOKEN : Authentication flow for refreshing the access token and ID token by supplying a valid refresh token.
CUSTOM_AUTH : Custom authentication flow.
ADMIN_NO_SRP_AUTH : Non-SRP authentication flow; you can pass in the USERNAME and PASSWORD directly if the flow is enabled for calling the app client.
USER_PASSWORD_AUTH : Non-SRP authentication flow; USERNAME and PASSWORD are passed directly. If a user migration Lambda trigger is set, this flow will invoke the user migration Lambda if the USERNAME is not found in the user pool.
ADMIN_USER_PASSWORD_AUTH : Admin-based user password authentication. This replaces the ADMIN_NO_SRP_AUTH authentication flow. In this flow, Cognito receives the password in the request instead of using the SRP process to verify passwords.

Possible values:

USER_SRP_AUTH
REFRESH_TOKEN_AUTH
REFRESH_TOKEN
CUSTOM_AUTH
ADMIN_NO_SRP_AUTH
USER_PASSWORD_AUTH
ADMIN_USER_PASSWORD_AUTH
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cognito-idp", "admin-initiate-auth", "user-pool-id", "client-id", "auth-flow", add_option_dict)
