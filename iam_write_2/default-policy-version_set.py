#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/set-default-policy-version.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # policy-arn : The Amazon Resource Name (ARN) of the IAM policy whose default version you want to set.
For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    # version-id : The version of the policy to set as the default (operative) version.
For more information about managed policy versions, see Versioning for Managed Policies in the IAM User Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "set-default-policy-version", "policy-arn", "version-id", add_option_dict)
