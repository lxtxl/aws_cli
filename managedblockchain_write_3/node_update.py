#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/update-node.html
if __name__ == '__main__':
    """
	create-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-node.html
	delete-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/delete-node.html
	get-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-node.html
	list-nodes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-nodes.html
    """

    parameter_display_string = """
    # network-id : The unique ID of the Managed Blockchain network to which the node belongs.
    # member-id : The unique ID of the member that owns the node.
    # node-id : The unique ID of the node.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("managedblockchain", "update-node", "network-id", "member-id", "node-id", add_option_dict)
