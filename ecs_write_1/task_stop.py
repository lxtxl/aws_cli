#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/stop-task.html
if __name__ == '__main__':
    """
	describe-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-tasks.html
	list-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-tasks.html
	run-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/run-task.html
	start-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/start-task.html
    """

    parameter_display_string = """
    # task : The task ID or full Amazon Resource Name (ARN) of the task to stop.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ecs", "stop-task", "task", add_option_dict)





