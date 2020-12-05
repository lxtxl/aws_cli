#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-load-balancer-target-groups.html
if __name__ == '__main__':
    """
	attach-load-balancer-target-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/attach-load-balancer-target-groups.html
	detach-load-balancer-target-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/detach-load-balancer-target-groups.html
    """

    parameter_display_string = """
    # auto-scaling-group-name : The name of the Auto Scaling group.
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

    execute_one_parameter("autoscaling", "describe-load-balancer-target-groups", "auto-scaling-group-name", add_option_dict)