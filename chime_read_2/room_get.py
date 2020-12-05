#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-room.html
if __name__ == '__main__':
    """
	create-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-room.html
	delete-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-room.html
	list-rooms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-rooms.html
	update-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-room.html
    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    # room-id : The room ID.
    """

    execute_two_parameter("chime", "get-room", "account-id", "room-id", parameter_display_string)