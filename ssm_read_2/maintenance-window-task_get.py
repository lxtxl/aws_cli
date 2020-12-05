#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window-task.html
if __name__ == '__main__':
    """
	describe-maintenance-window-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-tasks.html
	update-maintenance-window-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-maintenance-window-task.html
    """

    parameter_display_string = """
    # window-id : The maintenance window ID that includes the task to retrieve.
    # window-task-id : The maintenance window task ID to retrieve.
    """

    execute_two_parameter("ssm", "get-maintenance-window-task", "window-id", "window-task-id", parameter_display_string)