#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/register-cross-account-access-role.html
if __name__ == '__main__':
    """
	describe-cross-account-access-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-cross-account-access-role.html
    """

    parameter_display_string = """
    # role-arn : The ARN of the IAM role that grants Amazon Inspector access to AWS Services needed to perform security assessments.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("inspector", "register-cross-account-access-role", "role-arn", add_option_dict)





