#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-router.html
if __name__ == '__main__':
    """
	delete-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-router.html
	describe-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-router.html
	list-virtual-routers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-routers.html
	update-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-virtual-router.html
    """

    parameter_display_string = """
    # mesh-name : The name of the service mesh to create the virtual router in.
    # spec : 
    # virtual-router-name : The name to use for the virtual router.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("appmesh", "create-virtual-router", "mesh-name", "spec", "virtual-router-name", add_option_dict)
