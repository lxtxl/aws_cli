#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-auto-scaling-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-auto-scaling-group.html
	describe-auto-scaling-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-groups.html
	update-auto-scaling-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html
    """

    write_parameter("autoscaling", "create-auto-scaling-group")