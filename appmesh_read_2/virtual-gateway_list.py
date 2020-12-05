#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-gateway.html
if __name__ == '__main__':
    """
	create-virtual-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-gateway.html
	delete-virtual-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-gateway.html
	list-virtual-gateways : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-gateways.html
	update-virtual-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-virtual-gateway.html
    """

    parameter_display_string = """
    # mesh-name : The name of the service mesh that the gateway route resides in.
    # virtual-gateway-name : The name of the virtual gateway to describe.
    """

    execute_two_parameter("appmesh", "describe-virtual-gateway", "mesh-name", "virtual-gateway-name", parameter_display_string)