#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/list-conference-providers.html
if __name__ == '__main__':
    """
	create-conference-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-conference-provider.html
	delete-conference-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-conference-provider.html
	get-conference-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-conference-provider.html
	update-conference-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-conference-provider.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("alexaforbusiness", "list-conference-providers", add_option_dict)