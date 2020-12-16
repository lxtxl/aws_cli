#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-route.html
if __name__ == '__main__':
    """
	create-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-route.html
	describe-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-route.html
	list-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-routes.html
	update-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-route.html
    """

    parameter_display_string = """
    # mesh-name : The name of the service mesh to delete the route in.
    # route-name : The name of the route to delete.
    # virtual-router-name : The name of the virtual router to delete the route in.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("appmesh", "delete-route", "mesh-name", "route-name", "virtual-router-name", add_option_dict)
