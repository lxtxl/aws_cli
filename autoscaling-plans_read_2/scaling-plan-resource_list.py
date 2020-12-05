#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/describe-scaling-plan-resources.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # scaling-plan-name : The name of the scaling plan.
    # scaling-plan-version : 
    """

    execute_two_parameter("autoscaling-plans", "describe-scaling-plan-resources", "scaling-plan-name", "scaling-plan-version", parameter_display_string)