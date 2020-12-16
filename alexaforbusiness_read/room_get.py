#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-room.html
if __name__ == '__main__':
    """
	create-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-room.html
	delete-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-room.html
	resolve-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/resolve-room.html
	search-rooms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/search-rooms.html
	update-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-room.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("alexaforbusiness", "get-room", add_option_dict)