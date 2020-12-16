#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/set-instance-protection.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # instance-ids : One or more instance IDs. You can specify up to 50 instances.
(string)
    # auto-scaling-group-name : The name of the Auto Scaling group.
    # protected-from-scale-in | --no-protected-from-scale-in : Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling when scaling in.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("autoscaling", "set-instance-protection", "instance-ids", "auto-scaling-group-name", "protected-from-scale-in | --no-protected-from-scale-in", add_option_dict)
