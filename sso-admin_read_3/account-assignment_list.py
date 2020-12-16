#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-account-assignments.html
if __name__ == '__main__':
    """
	create-account-assignment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-account-assignment.html
	delete-account-assignment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-account-assignment.html
    """

    parameter_display_string = """
    # instance-arn : The ARN of the SSO instance under which the operation will be executed. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    # account-id : The identifier of the AWS account from which to list the assignments.
    """

    execute_two_parameter("sso-admin", "list-account-assignments", "instance-arn", "account-id", parameter_display_string)