#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/update-scaling-plan.html
if __name__ == '__main__':
    """
	create-scaling-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/create-scaling-plan.html
	delete-scaling-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/delete-scaling-plan.html
	describe-scaling-plans : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/describe-scaling-plans.html
    """

    parameter_display_string = """
    # scaling-plan-name : The name of the scaling plan.
    # scaling-plan-version : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("autoscaling-plans", "update-scaling-plan", "scaling-plan-name", "scaling-plan-version", add_option_dict)
