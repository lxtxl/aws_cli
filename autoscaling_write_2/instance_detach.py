#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/detach-instances.html
if __name__ == '__main__':
    """
	attach-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/attach-instances.html
    """

    parameter_display_string = """
    # auto-scaling-group-name : The name of the Auto Scaling group.
    # should-decrement-desired-capacity | --no-should-decrement-desired-capacity : Indicates whether the Auto Scaling group decrements the desired capacity value by the number of instances detached.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("autoscaling", "detach-instances", "auto-scaling-group-name", "should-decrement-desired-capacity | --no-should-decrement-desired-capacity", add_option_dict)
