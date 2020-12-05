#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/set-permission.html
if __name__ == '__main__':
    """
	describe-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-permissions.html
    """

    parameter_display_string = """
    # stack-id : The stack ID.
    # iam-user-arn : The userâs IAM ARN. This can also be a federated userâs ARN.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("opsworks", "set-permission", "stack-id", "iam-user-arn", add_option_dict)
