#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/deploy.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # service : The short name or full Amazon Resource Name (ARN) of the service to update
    # task-definition : The file path where your task definition file is located. The format of the file must be the same as the JSON output of:
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ecs", "deploy", "service", "task-definition", add_option_dict)
