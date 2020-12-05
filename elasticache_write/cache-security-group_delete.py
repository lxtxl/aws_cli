#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-cache-security-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-cache-security-group.html
	describe-cache-security-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-cache-security-groups.html
    """

    write_parameter("elasticache", "delete-cache-security-group")