#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/delete-cluster.html
	describe-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-clusters.html
	list-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-clusters.html
    """

    write_parameter("ecs", "create-cluster")