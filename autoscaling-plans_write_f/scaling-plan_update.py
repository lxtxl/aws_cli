#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-scaling-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/create-scaling-plan.html
	delete-scaling-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/delete-scaling-plan.html
	describe-scaling-plans : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/describe-scaling-plans.html
    """

    write_parameter("autoscaling-plans", "update-scaling-plan")