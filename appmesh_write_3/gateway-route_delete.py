#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-gateway-route.html
if __name__ == '__main__':
    """
	create-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-gateway-route.html
	describe-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-gateway-route.html
	list-gateway-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-gateway-routes.html
	update-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-gateway-route.html
    """

    parameter_display_string = """
    # gateway-route-name : The name of the gateway route to delete.
    # mesh-name : The name of the service mesh to delete the gateway route from.
    # virtual-gateway-name : The name of the virtual gateway to delete the route from.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("appmesh", "delete-gateway-route", "gateway-route-name", "mesh-name", "virtual-gateway-name", add_option_dict)
