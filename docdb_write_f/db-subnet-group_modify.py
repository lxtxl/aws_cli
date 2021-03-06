#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-db-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-db-subnet-group.html
	delete-db-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/delete-db-subnet-group.html
	describe-db-subnet-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-subnet-groups.html
    """

    write_parameter("docdb", "modify-db-subnet-group")