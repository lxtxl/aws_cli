#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/deregister-task-definition.html
if __name__ == '__main__':
    """
	describe-task-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-task-definition.html
	list-task-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-task-definitions.html
	register-task-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/register-task-definition.html
    """

    parameter_display_string = """
    # task-definition : The family and revision (family:revision ) or full Amazon Resource Name (ARN) of the task definition to deregister. You must specify a revision .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ecs", "deregister-task-definition", "task-definition", add_option_dict)





