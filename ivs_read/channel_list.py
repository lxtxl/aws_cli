#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-channels.html
if __name__ == '__main__':
    """
	create-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/create-channel.html
	delete-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/delete-channel.html
	get-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-channel.html
	update-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/update-channel.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("ivs", "list-channels", add_option_dict)