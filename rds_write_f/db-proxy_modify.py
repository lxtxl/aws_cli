#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-db-proxy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-proxy.html
	delete-db-proxy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-proxy.html
	describe-db-proxies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-proxies.html
    """

    write_parameter("rds", "modify-db-proxy")