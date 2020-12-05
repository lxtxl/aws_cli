#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-nodes.html
if __name__ == '__main__':
    """
	create-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-node.html
	delete-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/delete-node.html
	get-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-node.html
	update-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/update-node.html
    """

    parameter_display_string = """
    # network-id : The unique identifier of the network for which to list nodes.
    # member-id : The unique identifier of the member who owns the nodes to list.
    """

    execute_two_parameter("managedblockchain", "list-nodes", "network-id", "member-id", parameter_display_string)