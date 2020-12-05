#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-routes.html
if __name__ == '__main__':
    """
	create-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-route.html
	delete-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-route.html
	describe-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-route.html
	update-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-route.html
    """

    parameter_display_string = """
    # mesh-name : The name of the service mesh to list routes in.
    # virtual-router-name : The name of the virtual router to list routes in.
    """

    execute_two_parameter("appmesh", "list-routes", "mesh-name", "virtual-router-name", parameter_display_string)