#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/create-grant-version.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # client-token : Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
    # grant-arn : Amazon Resource Name (ARN) of the grant.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("license-manager", "create-grant-version", "client-token", "grant-arn", add_option_dict)
