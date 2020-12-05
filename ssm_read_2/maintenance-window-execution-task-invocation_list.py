#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-execution-task-invocations.html
if __name__ == '__main__':
    """
	get-maintenance-window-execution-task-invocation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window-execution-task-invocation.html
    """

    parameter_display_string = """
    # window-execution-id : The ID of the maintenance window execution the task is part of.
    # task-id : The ID of the specific task in the maintenance window task that should be retrieved.
    """

    execute_two_parameter("ssm", "describe-maintenance-window-execution-task-invocations", "window-execution-id", "task-id", parameter_display_string)