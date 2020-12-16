#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-tasks.html
if __name__ == '__main__':
    """
	describe-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-tasks.html
	run-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/run-task.html
	start-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/start-task.html
	stop-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/stop-task.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("ecs", "list-tasks", add_option_dict)