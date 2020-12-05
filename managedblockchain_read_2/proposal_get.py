#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-proposal.html
if __name__ == '__main__':
    """
	create-proposal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-proposal.html
	list-proposals : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-proposals.html
    """

    parameter_display_string = """
    # network-id : The unique identifier of the network for which the proposal is made.
    # proposal-id : The unique identifier of the proposal.
    """

    execute_two_parameter("managedblockchain", "get-proposal", "network-id", "proposal-id", parameter_display_string)