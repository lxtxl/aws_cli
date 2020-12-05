#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-resource-definitions.html
if __name__ == '__main__':
    """
	create-resource-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-resource-definition.html
	delete-resource-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-resource-definition.html
	get-resource-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-resource-definition.html
	update-resource-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-resource-definition.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("greengrass", "list-resource-definitions", add_option_dict)