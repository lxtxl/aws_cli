#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-proposal-votes.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # network-id : The unique identifier of the network.
    # proposal-id : The unique identifier of the proposal.
    """

    execute_two_parameter("managedblockchain", "list-proposal-votes", "network-id", "proposal-id", parameter_display_string)