#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/terminate-instance-in-auto-scaling-group.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # instance-id : The ID of the instance.
    # should-decrement-desired-capacity | --no-should-decrement-desired-capacity : Indicates whether terminating the instance also decrements the size of the Auto Scaling group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("autoscaling", "terminate-instance-in-auto-scaling-group", "instance-id", "should-decrement-desired-capacity | --no-should-decrement-desired-capacity", add_option_dict)
