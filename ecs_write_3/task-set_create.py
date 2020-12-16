#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/create-task-set.html
if __name__ == '__main__':
    """
	delete-task-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/delete-task-set.html
	describe-task-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-task-sets.html
	update-task-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-task-set.html
    """

    parameter_display_string = """
    # service : The short name or full Amazon Resource Name (ARN) of the service to create the task set in.
    # cluster : The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.
    # task-definition : The task definition for the tasks in the task set to use.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ecs", "create-task-set", "service", "cluster", "task-definition", add_option_dict)
