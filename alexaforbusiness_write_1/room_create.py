#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-room.html
if __name__ == '__main__':
    """
	delete-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-room.html
	get-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-room.html
	resolve-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/resolve-room.html
	search-rooms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/search-rooms.html
	update-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-room.html
    """

    parameter_display_string = """
    # room-name : The name for the room.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("alexaforbusiness", "create-room", "room-name", add_option_dict)





