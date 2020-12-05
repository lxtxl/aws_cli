#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-managed-instance-role.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # instance-id : The ID of the managed instance where you want to update the role.
    # iam-role : The IAM role you want to assign or change.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ssm", "update-managed-instance-role", "instance-id", "iam-role", add_option_dict)
