#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-room-membership.html
if __name__ == '__main__':
    """
	delete-room-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-room-membership.html
	list-room-memberships : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-room-memberships.html
	update-room-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-room-membership.html
    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    # room-id : The room ID.
    # member-id : The Amazon Chime member ID (user ID or bot ID).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("chime", "create-room-membership", "account-id", "room-id", "member-id", add_option_dict)
