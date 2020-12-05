#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-member.html
if __name__ == '__main__':
    """
	create-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-member.html
	delete-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/delete-member.html
	list-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-members.html
	update-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/update-member.html
    """

    parameter_display_string = """
    # network-id : The unique identifier of the network to which the member belongs.
    # member-id : The unique identifier of the member.
    """

    execute_two_parameter("managedblockchain", "get-member", "network-id", "member-id", parameter_display_string)