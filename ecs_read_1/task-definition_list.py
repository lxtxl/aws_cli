#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-task-definition.html
if __name__ == '__main__':
    """
	deregister-task-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/deregister-task-definition.html
	list-task-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-task-definitions.html
	register-task-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/register-task-definition.html
    """

    parameter_display_string = """
    # task-definition : The family for the latest ACTIVE revision, family and revision (family:revision ) for a specific revision in the family, or full Amazon Resource Name (ARN) of the task definition to describe.
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

    execute_one_parameter("ecs", "describe-task-definition", "task-definition", add_option_dict)