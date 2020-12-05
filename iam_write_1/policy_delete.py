#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-policy.html
if __name__ == '__main__':
    """
	create-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-policy.html
	get-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-policy.html
	list-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-policies.html
    """

    parameter_display_string = """
    # policy-arn : The Amazon Resource Name (ARN) of the IAM policy you want to delete.
For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "delete-policy", "policy-arn", add_option_dict)





