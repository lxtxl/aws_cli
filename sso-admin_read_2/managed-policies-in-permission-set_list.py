#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-managed-policies-in-permission-set.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # instance-arn : The ARN of the SSO instance under which the operation will be executed. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    # permission-set-arn : The ARN of the  PermissionSet whose managed policies will be listed.
    """

    execute_two_parameter("sso-admin", "list-managed-policies-in-permission-set", "instance-arn", "permission-set-arn", parameter_display_string)