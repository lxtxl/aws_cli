#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-router.html
if __name__ == '__main__':
    """
	create-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-router.html
	describe-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-router.html
	list-virtual-routers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-routers.html
	update-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-virtual-router.html
    """

    parameter_display_string = """
    # mesh-name : The name of the service mesh to delete the virtual router in.
    # virtual-router-name : The name of the virtual router to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("appmesh", "delete-virtual-router", "mesh-name", "virtual-router-name", add_option_dict)
