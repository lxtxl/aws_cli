#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/list-gateway-groups.html
if __name__ == '__main__':
    """
	create-gateway-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-gateway-group.html
	delete-gateway-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-gateway-group.html
	get-gateway-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-gateway-group.html
	update-gateway-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-gateway-group.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("alexaforbusiness", "list-gateway-groups", add_option_dict)