#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/enable-metrics-collection.html
if __name__ == '__main__':
    """
	disable-metrics-collection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/disable-metrics-collection.html
    """

    parameter_display_string = """
    # auto-scaling-group-name : The name of the Auto Scaling group.
    # granularity : The granularity to associate with the metrics to collect. The only valid value is 1Minute .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("autoscaling", "enable-metrics-collection", "auto-scaling-group-name", "granularity", add_option_dict)
