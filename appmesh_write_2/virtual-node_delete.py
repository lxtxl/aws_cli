#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-node.html
if __name__ == '__main__':
    """
	create-virtual-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-node.html
	describe-virtual-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-node.html
	list-virtual-nodes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-nodes.html
	update-virtual-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-virtual-node.html
    """

    parameter_display_string = """
    # mesh-name : The name of the service mesh to delete the virtual node in.
    # virtual-node-name : The name of the virtual node to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("appmesh", "delete-virtual-node", "mesh-name", "virtual-node-name", add_option_dict)
