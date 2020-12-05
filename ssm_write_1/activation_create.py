#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-activation.html
if __name__ == '__main__':
    """
	delete-activation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-activation.html
	describe-activations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-activations.html
    """

    parameter_display_string = """
    # iam-role : The Amazon Identity and Access Management (IAM) role that you want to assign to the managed instance. This IAM role must provide AssumeRole permissions for the Systems Manager service principal ssm.amazonaws.com . For more information, see Create an IAM service role for a hybrid environment in the AWS Systems Manager User Guide .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ssm", "create-activation", "iam-role", add_option_dict)





