#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service-primary-task-set.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # cluster : The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set exists in.
    # service : The short name or full Amazon Resource Name (ARN) of the service that the task set exists in.
    # primary-task-set : The short name or full Amazon Resource Name (ARN) of the task set to set as the primary task set in the deployment.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ecs", "update-service-primary-task-set", "cluster", "service", "primary-task-set", add_option_dict)
