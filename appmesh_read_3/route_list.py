#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-route.html
if __name__ == '__main__':
    """
	create-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-route.html
	delete-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-route.html
	list-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-routes.html
	update-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-route.html
    """

    parameter_display_string = """
    # mesh-name : The name of the service mesh that the route resides in.
    # route-name : The name of the route to describe.
    """

    execute_two_parameter("appmesh", "describe-route", "mesh-name", "route-name", parameter_display_string)