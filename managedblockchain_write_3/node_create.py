#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-node.html
if __name__ == '__main__':
    """
	delete-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/delete-node.html
	get-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-node.html
	list-nodes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-nodes.html
	update-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/update-node.html
    """

    parameter_display_string = """
    # network-id : The unique identifier of the network in which this node runs.
    # member-id : The unique identifier of the member that owns this node.
    # node-configuration : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("managedblockchain", "create-node", "network-id", "member-id", "node-configuration", add_option_dict)
