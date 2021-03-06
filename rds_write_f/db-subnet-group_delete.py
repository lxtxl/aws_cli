#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-db-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-subnet-group.html
	describe-db-subnet-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-subnet-groups.html
	modify-db-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-subnet-group.html
    """

    write_parameter("rds", "delete-db-subnet-group")