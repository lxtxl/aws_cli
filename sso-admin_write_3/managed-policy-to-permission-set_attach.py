#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/attach-managed-policy-to-permission-set.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # instance-arn : The ARN of the SSO instance under which the operation will be executed. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    # permission-set-arn : The ARN of the  PermissionSet that the managed policy should be attached to.
    # managed-policy-arn : The IAM managed policy ARN to be attached to a permission set.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("sso-admin", "attach-managed-policy-to-permission-set", "instance-arn", "permission-set-arn", "managed-policy-arn", add_option_dict)
