#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/resolve-room.html
if __name__ == '__main__':
    """
	create-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-room.html
	delete-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-room.html
	get-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-room.html
	search-rooms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/search-rooms.html
	update-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-room.html
    """

    parameter_display_string = """
    # user-id : The ARN of the user. Required.
    # skill-id : The ARN of the skill that was requested. Required.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("alexaforbusiness", "resolve-room", "user-id", "skill-id", add_option_dict)
