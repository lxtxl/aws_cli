#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/batch-delete-scheduled-action.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # auto-scaling-group-name : The name of the Auto Scaling group.
    # scheduled-action-names : The names of the scheduled actions to delete. The maximum number allowed is 50.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("autoscaling", "batch-delete-scheduled-action", "auto-scaling-group-name", "scheduled-action-names", add_option_dict)
