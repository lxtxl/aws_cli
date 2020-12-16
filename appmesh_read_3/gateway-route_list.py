#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-gateway-route.html
if __name__ == '__main__':
    """
	create-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-gateway-route.html
	delete-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-gateway-route.html
	list-gateway-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-gateway-routes.html
	update-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-gateway-route.html
    """

    parameter_display_string = """
    # gateway-route-name : The name of the gateway route to describe.
    # mesh-name : The name of the service mesh that the gateway route resides in.
    """

    execute_two_parameter("appmesh", "describe-gateway-route", "gateway-route-name", "mesh-name", parameter_display_string)