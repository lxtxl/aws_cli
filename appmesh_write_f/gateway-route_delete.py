#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-gateway-route.html
	describe-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-gateway-route.html
	list-gateway-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-gateway-routes.html
	update-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-gateway-route.html
    """

    write_parameter("appmesh", "delete-gateway-route")