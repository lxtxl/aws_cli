#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-replication-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-subnet-group.html
	describe-replication-subnet-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-subnet-groups.html
	modify-replication-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-subnet-group.html
    """

    write_parameter("dms", "delete-replication-subnet-group")