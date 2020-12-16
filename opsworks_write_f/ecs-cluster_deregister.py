#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-ecs-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-ecs-clusters.html
	register-ecs-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-ecs-cluster.html
    """

    write_parameter("opsworks", "deregister-ecs-cluster")