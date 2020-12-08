#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-local-gateway-route-table-vpc-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-local-gateway-route-table-vpc-association.html
	describe-local-gateway-route-table-vpc-associations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-local-gateway-route-table-vpc-associations.html
    """

    write_parameter("ec2", "delete-local-gateway-route-table-vpc-association")