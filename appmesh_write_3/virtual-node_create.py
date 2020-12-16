#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-node.html
if __name__ == '__main__':
    """
	delete-virtual-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-node.html
	describe-virtual-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-node.html
	list-virtual-nodes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-nodes.html
	update-virtual-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-virtual-node.html
    """

    parameter_display_string = """
    # mesh-name : The name of the service mesh to create the virtual node in.
    # spec : 
    # virtual-node-name : The name to use for the virtual node.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("appmesh", "create-virtual-node", "mesh-name", "spec", "virtual-node-name", add_option_dict)
