#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	disable-transit-gateway-route-table-propagation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-transit-gateway-route-table-propagation.html
	get-transit-gateway-route-table-propagations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-transit-gateway-route-table-propagations.html
    """

    write_parameter("ec2", "enable-transit-gateway-route-table-propagation")