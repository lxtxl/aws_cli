#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-cache-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-cache-subnet-group.html
	describe-cache-subnet-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-cache-subnet-groups.html
	modify-cache-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-cache-subnet-group.html
    """

    write_parameter("elasticache", "create-cache-subnet-group")