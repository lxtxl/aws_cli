#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/attach-load-balancer-target-groups.html
if __name__ == '__main__':
    """
	describe-load-balancer-target-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-load-balancer-target-groups.html
	detach-load-balancer-target-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/detach-load-balancer-target-groups.html
    """

    parameter_display_string = """
    # auto-scaling-group-name : The name of the Auto Scaling group.
    # target-group-arns : The Amazon Resource Names (ARN) of the target groups. You can specify up to 10 target groups. To get the ARN of a target group, use the Elastic Load Balancing DescribeTargetGroups API operation.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("autoscaling", "attach-load-balancer-target-groups", "auto-scaling-group-name", "target-group-arns", add_option_dict)
