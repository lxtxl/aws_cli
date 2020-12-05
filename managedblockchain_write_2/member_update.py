#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/update-member.html
if __name__ == '__main__':
    """
	create-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-member.html
	delete-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/delete-member.html
	get-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-member.html
	list-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-members.html
    """

    parameter_display_string = """
    # network-id : The unique ID of the Managed Blockchain network to which the member belongs.
    # member-id : The unique ID of the member.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("managedblockchain", "update-member", "network-id", "member-id", add_option_dict)
