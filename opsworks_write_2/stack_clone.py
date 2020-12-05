#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/clone-stack.html
if __name__ == '__main__':
    """
	create-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-stack.html
	delete-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/delete-stack.html
	describe-stacks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-stacks.html
	start-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/start-stack.html
	stop-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/stop-stack.html
	update-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-stack.html
    """

    parameter_display_string = """
    # source-stack-id : The source stack ID.
    # service-role-arn : The stack AWS Identity and Access Management (IAM) role, which allows AWS OpsWorks Stacks to work with AWS resources on your behalf. You must set this parameter to the Amazon Resource Name (ARN) for an existing IAM role. If you create a stack by using the AWS OpsWorks Stacks console, it creates the role for you. You can obtain an existing stackâs IAM ARN programmatically by calling  DescribePermissions . For more information about IAM ARNs, see Using Identifiers .

Note
You must set this parameter to a valid service role ARN or the action will fail; there is no default value. You can specify the source stackâs service role ARN, if you prefer, but you must do so explicitly.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("opsworks", "clone-stack", "source-stack-id", "service-role-arn", add_option_dict)
