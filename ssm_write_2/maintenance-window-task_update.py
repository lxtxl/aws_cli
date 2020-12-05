#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-maintenance-window-task.html
if __name__ == '__main__':
    """
	describe-maintenance-window-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-tasks.html
	get-maintenance-window-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window-task.html
    """

    parameter_display_string = """
    # window-id : The maintenance window ID that contains the task to modify.
    # window-task-id : The task ID to modify.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ssm", "update-maintenance-window-task", "window-id", "window-task-id", add_option_dict)
