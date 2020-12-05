#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/attach-load-balancers.html
if __name__ == '__main__':
    """
	describe-load-balancers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-load-balancers.html
	detach-load-balancers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/detach-load-balancers.html
    """

    parameter_display_string = """
    # auto-scaling-group-name : The name of the Auto Scaling group.
    # load-balancer-names : The names of the load balancers. You can specify up to 10 load balancers.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("autoscaling", "attach-load-balancers", "auto-scaling-group-name", "load-balancer-names", add_option_dict)
