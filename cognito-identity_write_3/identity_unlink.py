#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/unlink-identity.html
if __name__ == '__main__':
    """
	delete-identities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/delete-identities.html
	describe-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/describe-identity.html
	list-identities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/list-identities.html
    """

    parameter_display_string = """
    # identity-id : A unique identifier in the format REGION:GUID.
    # logins : A set of optional name-value pairs that map provider names to provider tokens.
key -> (string)
value -> (string)
    # logins-to-remove : Provider names to unlink from this identity.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cognito-identity", "unlink-identity", "identity-id", "logins", "logins-to-remove", add_option_dict)
