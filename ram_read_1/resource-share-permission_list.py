#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/list-resource-share-permissions.html
if __name__ == '__main__':
    """
	associate-resource-share-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/associate-resource-share-permission.html
	disassociate-resource-share-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/disassociate-resource-share-permission.html
    """

    parameter_display_string = """
    # resource-share-arn : The Amazon Resource Name (ARN) of the resource share.
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

    execute_one_parameter("ram", "list-resource-share-permissions", "resource-share-arn", add_option_dict)