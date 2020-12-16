#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-virtual-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-gateway.html
	delete-virtual-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-gateway.html
	describe-virtual-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-gateway.html
	list-virtual-gateways : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-gateways.html
    """

    write_parameter("appmesh", "update-virtual-gateway")