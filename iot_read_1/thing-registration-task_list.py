#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-thing-registration-task.html
if __name__ == '__main__':
    """
	list-thing-registration-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-registration-tasks.html
	start-thing-registration-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/start-thing-registration-task.html
	stop-thing-registration-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/stop-thing-registration-task.html
    """

    parameter_display_string = """
    # task-id : The task ID.
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

    execute_one_parameter("iot", "describe-thing-registration-task", "task-id", add_option_dict)