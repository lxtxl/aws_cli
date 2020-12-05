#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/start-instance-refresh.html
if __name__ == '__main__':
    """
	cancel-instance-refresh : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/cancel-instance-refresh.html
	describe-instance-refreshes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-instance-refreshes.html
    """

    parameter_display_string = """
    # auto-scaling-group-name : The name of the Auto Scaling group.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("autoscaling", "start-instance-refresh", "auto-scaling-group-name", add_option_dict)





