#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-room.html
if __name__ == '__main__':
    """
	create-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-room.html
	delete-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-room.html
	get-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-room.html
	list-rooms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-rooms.html
    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    # room-id : The room ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "update-room", "account-id", "room-id", add_option_dict)
