#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-cache-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-cache-parameter-group.html
	delete-cache-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-cache-parameter-group.html
	describe-cache-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-cache-parameter-groups.html
	reset-cache-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/reset-cache-parameter-group.html
    """

    write_parameter("elasticache", "modify-cache-parameter-group")