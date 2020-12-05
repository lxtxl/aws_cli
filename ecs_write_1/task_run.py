#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/run-task.html
if __name__ == '__main__':
    """
	describe-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-tasks.html
	list-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-tasks.html
	start-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/start-task.html
	stop-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/stop-task.html
    """

    parameter_display_string = """
    # task-definition : The family and revision (family:revision ) or full ARN of the task definition to run. If a revision is not specified, the latest ACTIVE revision is used.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ecs", "run-task", "task-definition", add_option_dict)





