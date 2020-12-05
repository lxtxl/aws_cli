#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-policy-versions.html
if __name__ == '__main__':
    """
	create-policy-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-policy-version.html
	delete-policy-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-policy-version.html
	get-policy-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-policy-version.html
    """

    parameter_display_string = """
    # policy-arn : The Amazon Resource Name (ARN) of the IAM policy for which you want the versions.
For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
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

    execute_one_parameter("iam", "list-policy-versions", "policy-arn", add_option_dict)