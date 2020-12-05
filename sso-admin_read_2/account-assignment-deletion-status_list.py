#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-account-assignment-deletion-status.html
if __name__ == '__main__':
    """
	list-account-assignment-deletion-status : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-account-assignment-deletion-status.html
    """

    parameter_display_string = """
    # instance-arn : The ARN of the SSO instance under which the operation will be executed. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    # account-assignment-deletion-request-id : The identifier that is used to track the request operation progress.
    """

    execute_two_parameter("sso-admin", "describe-account-assignment-deletion-status", "instance-arn", "account-assignment-deletion-request-id", parameter_display_string)