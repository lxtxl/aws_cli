#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/delete-task-set.html
if __name__ == '__main__':
    """
	create-task-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/create-task-set.html
	describe-task-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-task-sets.html
	update-task-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-task-set.html
    """

    parameter_display_string = """
    # cluster : The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set exists in to delete.
    # service : The short name or full Amazon Resource Name (ARN) of the service that hosts the task set to delete.
    # task-set : The task set ID or full Amazon Resource Name (ARN) of the task set to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ecs", "delete-task-set", "cluster", "service", "task-set", add_option_dict)
