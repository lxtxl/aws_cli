#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-task-from-maintenance-window.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # window-id : The ID of the maintenance window the task should be removed from.
    # window-task-id : The ID of the task to remove from the maintenance window.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ssm", "deregister-task-from-maintenance-window", "window-id", "window-task-id", add_option_dict)
