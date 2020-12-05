#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-node.html
if __name__ == '__main__':
    """
	create-virtual-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-node.html
	delete-virtual-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-node.html
	list-virtual-nodes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-nodes.html
	update-virtual-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-virtual-node.html
    """

    parameter_display_string = """
    # mesh-name : The name of the service mesh that the virtual node resides in.
    # virtual-node-name : The name of the virtual node to describe.
    """

    execute_two_parameter("appmesh", "describe-virtual-node", "mesh-name", "virtual-node-name", parameter_display_string)