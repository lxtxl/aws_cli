#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-global-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-global-cluster.html
	describe-global-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-global-clusters.html
	modify-global-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-global-cluster.html
    """

    write_parameter("rds", "delete-global-cluster")