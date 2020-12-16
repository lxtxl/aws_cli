#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-oidc/start-device-authorization.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # client-id : The unique identifier string for the client that is registered with AWS SSO. This value should come from the persisted result of the  RegisterClient API operation.
    # client-secret : A secret string that is generated for the client. This value should come from the persisted result of the  RegisterClient API operation.
    # start-url : The URL for the AWS SSO user portal. For more information, see Using the User Portal in the AWS Single Sign-On User Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("sso-oidc", "start-device-authorization", "client-id", "client-secret", "start-url", add_option_dict)
