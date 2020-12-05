#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-command-invocation.html
if __name__ == '__main__':
    """
	list-command-invocations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-command-invocations.html
    """

    parameter_display_string = """
    # command-id : (Required) The parent command ID of the invocation plugin.
    # instance-id : (Required) The ID of the managed instance targeted by the command. A managed instance can be an EC2 instance or an instance in your hybrid environment that is configured for Systems Manager.
    """

    execute_two_parameter("ssm", "get-command-invocation", "command-id", "instance-id", parameter_display_string)