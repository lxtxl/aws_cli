#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window-execution-task-invocation.html
if __name__ == '__main__':
    """
	describe-maintenance-window-execution-task-invocations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-execution-task-invocations.html
    """

    parameter_display_string = """
    # window-execution-id : The ID of the maintenance window execution for which the task is a part.
    # task-id : The ID of the specific task in the maintenance window task that should be retrieved.
    """

    execute_two_parameter("ssm", "get-maintenance-window-execution-task-invocation", "window-execution-id", "task-id", parameter_display_string)