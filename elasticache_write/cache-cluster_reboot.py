#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-cache-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-cache-cluster.html
	delete-cache-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-cache-cluster.html
	describe-cache-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-cache-clusters.html
	modify-cache-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-cache-cluster.html
    """

    write_parameter("elasticache", "reboot-cache-cluster")