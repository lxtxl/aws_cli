#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-room-memberships.html
if __name__ == '__main__':
    """
	create-room-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-room-membership.html
	delete-room-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-room-membership.html
	update-room-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-room-membership.html
    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    # room-id : The room ID.
    """

    execute_two_parameter("chime", "list-room-memberships", "account-id", "room-id", parameter_display_string)