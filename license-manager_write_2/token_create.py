#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/create-token.html
if __name__ == '__main__':
    """
	delete-token : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/delete-token.html
	list-tokens : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/list-tokens.html
    """

    parameter_display_string = """
    # license-arn : Amazon Resource Name (ARN) of the license. The ARN is mapped to the aud claim of the JWT token.
    # client-token : Idempotency token, valid for 10 minutes.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("license-manager", "create-token", "license-arn", "client-token", add_option_dict)
