#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-tags-for-resource.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # instance-arn : The ARN of the SSO instance under which the operation will be executed. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    # resource-arn : The ARN of the resource with the tags to be listed.
    """

    execute_two_parameter("sso-admin", "list-tags-for-resource", "instance-arn", "resource-arn", parameter_display_string)