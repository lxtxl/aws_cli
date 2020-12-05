#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-scheduled-action.html
if __name__ == '__main__':
    """
	describe-scheduled-actions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-scheduled-actions.html
    """

    parameter_display_string = """
    # auto-scaling-group-name : The name of the Auto Scaling group.
    # scheduled-action-name : The name of the action to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("autoscaling", "delete-scheduled-action", "auto-scaling-group-name", "scheduled-action-name", add_option_dict)
