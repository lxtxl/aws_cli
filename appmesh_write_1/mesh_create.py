#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-mesh.html
if __name__ == '__main__':
    """
	delete-mesh : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-mesh.html
	describe-mesh : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-mesh.html
	list-meshes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-meshes.html
	update-mesh : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-mesh.html
    """

    parameter_display_string = """
    # mesh-name : The name to use for the service mesh.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("appmesh", "create-mesh", "mesh-name", add_option_dict)





