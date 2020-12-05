#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-user-permissions-boundary.html
if __name__ == '__main__':
    """
	delete-user-permissions-boundary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user-permissions-boundary.html
    """

    parameter_display_string = """
    # user-name : The name (friendly name, not ARN) of the IAM user for which you want to set the permissions boundary.
    # permissions-boundary : The ARN of the policy that is used to set the permissions boundary for the user.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "put-user-permissions-boundary", "user-name", "permissions-boundary", add_option_dict)
