#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-proposal.html
if __name__ == '__main__':
    """
	get-proposal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-proposal.html
	list-proposals : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-proposals.html
    """

    parameter_display_string = """
    # network-id : The unique identifier of the network for which the proposal is made.
    # member-id : The unique identifier of the member that is creating the proposal. This identifier is especially useful for identifying the member making the proposal when multiple members exist in a single AWS account.
    # actions : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("managedblockchain", "create-proposal", "network-id", "member-id", "actions", add_option_dict)
