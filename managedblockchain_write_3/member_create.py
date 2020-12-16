#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-member.html
if __name__ == '__main__':
    """
	delete-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/delete-member.html
	get-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-member.html
	list-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-members.html
	update-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/update-member.html
    """

    parameter_display_string = """
    # invitation-id : The unique identifier of the invitation that is sent to the member to join the network.
    # network-id : The unique identifier of the network in which the member is created.
    # member-configuration : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("managedblockchain", "create-member", "invitation-id", "network-id", "member-configuration", add_option_dict)
