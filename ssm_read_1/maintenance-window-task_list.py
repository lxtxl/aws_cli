#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-tasks.html
if __name__ == '__main__':
    """
	get-maintenance-window-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window-task.html
	update-maintenance-window-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-maintenance-window-task.html
    """

    parameter_display_string = """
    # window-id : The ID of the maintenance window whose tasks should be retrieved.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("ssm", "describe-maintenance-window-tasks", "window-id", add_option_dict)