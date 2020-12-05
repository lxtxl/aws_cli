#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-tasks.html
if __name__ == '__main__':
    """
	list-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-tasks.html
	run-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/run-task.html
	start-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/start-task.html
	stop-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/stop-task.html
    """

    parameter_display_string = """
    # tasks : A list of up to 100 task IDs or full ARN entries.
(string)
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

    execute_one_parameter("ecs", "describe-tasks", "tasks", add_option_dict)