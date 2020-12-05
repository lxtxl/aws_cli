#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/get-resource-shares.html
if __name__ == '__main__':
    """
	associate-resource-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/associate-resource-share.html
	create-resource-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/create-resource-share.html
	delete-resource-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/delete-resource-share.html
	disassociate-resource-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/disassociate-resource-share.html
	update-resource-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/update-resource-share.html
    """

    parameter_display_string = """
    # resource-owner : The type of owner.
Possible values:

SELF
OTHER-ACCOUNTS
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

    execute_one_parameter("ram", "get-resource-shares", "resource-owner", add_option_dict)