#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	associate-transit-gateway-route-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-transit-gateway-route-table.html
	create-transit-gateway-route-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-route-table.html
	delete-transit-gateway-route-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-route-table.html
	describe-transit-gateway-route-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-transit-gateway-route-tables.html
    """

    write_parameter("ec2", "disassociate-transit-gateway-route-table")