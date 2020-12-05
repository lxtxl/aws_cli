#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-members.html
if __name__ == '__main__':
    """
	create-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-member.html
	delete-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/delete-member.html
	get-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-member.html
	update-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/update-member.html
    """

    parameter_display_string = """
    # network-id : The unique identifier of the network for which to list members.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("managedblockchain", "list-members", "network-id", add_option_dict)