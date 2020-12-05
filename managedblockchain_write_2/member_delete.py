#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/delete-member.html
if __name__ == '__main__':
    """
	create-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-member.html
	get-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-member.html
	list-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-members.html
	update-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/update-member.html
    """

    parameter_display_string = """
    # network-id : The unique identifier of the network from which the member is removed.
    # member-id : The unique identifier of the member to remove.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("managedblockchain", "delete-member", "network-id", "member-id", add_option_dict)
