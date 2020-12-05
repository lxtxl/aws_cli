#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/start-task.html
if __name__ == '__main__':
    """
	describe-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-tasks.html
	list-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-tasks.html
	run-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/run-task.html
	stop-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/stop-task.html
    """

    parameter_display_string = """
    # container-instances : The container instance IDs or full ARN entries for the container instances on which you would like to place your task. You can specify up to 10 container instances.
(string)
    # task-definition : The family and revision (family:revision ) or full ARN of the task definition to start. If a revision is not specified, the latest ACTIVE revision is used.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ecs", "start-task", "container-instances", "task-definition", add_option_dict)
