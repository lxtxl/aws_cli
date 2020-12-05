#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-fargate-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-fargate-profile.html
	describe-fargate-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-fargate-profile.html
	list-fargate-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-fargate-profiles.html
    """

    write_parameter("eks", "delete-fargate-profile")