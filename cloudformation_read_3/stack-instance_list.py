#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-instance.html
if __name__ == '__main__':
    """
	create-stack-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack-instances.html
	delete-stack-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-stack-instances.html
	list-stack-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-instances.html
	update-stack-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack-instances.html
    """

    parameter_display_string = """
    # stack-set-name : The name or the unique stack ID of the stack set that you want to get stack instance information for.
    # stack-instance-account : The ID of an AWS account thatâs associated with this stack instance.
    """

    execute_two_parameter("cloudformation", "describe-stack-instance", "stack-set-name", "stack-instance-account", parameter_display_string)