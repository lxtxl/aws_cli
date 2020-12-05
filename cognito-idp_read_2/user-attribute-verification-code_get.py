#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-user-attribute-verification-code.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # access-token : The access token returned by the server response to get the user attribute verification code.
    # attribute-name : The attribute name returned by the server response to get the user attribute verification code.
    """

    execute_two_parameter("cognito-idp", "get-user-attribute-verification-code", "access-token", "attribute-name", parameter_display_string)