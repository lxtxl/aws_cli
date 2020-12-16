#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-virtual-router.html
if __name__ == '__main__':
    """
	create-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-router.html
	delete-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-router.html
	describe-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-router.html
	list-virtual-routers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-routers.html
    """

    parameter_display_string = """
    # mesh-name : The name of the service mesh that the virtual router resides in.
    # spec : 
    # virtual-router-name : The name of the virtual router to update.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("appmesh", "update-virtual-router", "mesh-name", "spec", "virtual-router-name", add_option_dict)
