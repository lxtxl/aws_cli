#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-db-cluster-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-cluster-endpoint.html
	delete-db-cluster-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-cluster-endpoint.html
	describe-db-cluster-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-cluster-endpoints.html
    """

    write_parameter("rds", "modify-db-cluster-endpoint")