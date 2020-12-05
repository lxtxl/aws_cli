#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-task-sets.html
if __name__ == '__main__':
    """
	create-task-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/create-task-set.html
	delete-task-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/delete-task-set.html
	update-task-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-task-set.html
    """

    parameter_display_string = """
    # cluster : The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.
    # service : The short name or full Amazon Resource Name (ARN) of the service that the task sets exist in.
    """

    execute_two_parameter("ecs", "describe-task-sets", "cluster", "service", parameter_display_string)