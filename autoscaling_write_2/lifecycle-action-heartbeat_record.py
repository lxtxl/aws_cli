#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/record-lifecycle-action-heartbeat.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # lifecycle-hook-name : The name of the lifecycle hook.
    # auto-scaling-group-name : The name of the Auto Scaling group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("autoscaling", "record-lifecycle-action-heartbeat", "lifecycle-hook-name", "auto-scaling-group-name", add_option_dict)
