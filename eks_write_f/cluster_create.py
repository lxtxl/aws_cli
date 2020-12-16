#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/delete-cluster.html
	describe-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-cluster.html
	list-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-clusters.html
    """

    write_parameter("eks", "create-cluster")