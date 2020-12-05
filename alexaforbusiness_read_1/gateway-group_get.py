#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-gateway-group.html
if __name__ == '__main__':
    """
	create-gateway-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-gateway-group.html
	delete-gateway-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-gateway-group.html
	list-gateway-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/list-gateway-groups.html
	update-gateway-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-gateway-group.html
    """

    parameter_display_string = """
    # gateway-group-arn : The ARN of the gateway group to get.
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

    execute_one_parameter("alexaforbusiness", "get-gateway-group", "gateway-group-arn", add_option_dict)