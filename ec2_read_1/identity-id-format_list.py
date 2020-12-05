#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-identity-id-format.html
if __name__ == '__main__':
    """
	modify-identity-id-format : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-identity-id-format.html
    """

    parameter_display_string = """
    # principal-arn : The ARN of the principal, which can be an IAM role, IAM user, or the root user.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("ec2", "describe-identity-id-format", "principal-arn", add_option_dict)