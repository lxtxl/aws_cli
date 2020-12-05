#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-replication-group.html
	delete-replication-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-replication-group.html
	describe-replication-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-replication-groups.html
    """

    write_parameter("elasticache", "modify-replication-group")