#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/batch-create-room-membership.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    # room-id : The room ID.
    # membership-item-list : The list of membership items.
(structure)

Membership details, such as member ID and member role.
MemberId -> (string)

The member ID.

Role -> (string)

The member role.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("chime", "batch-create-room-membership", "account-id", "room-id", "membership-item-list", add_option_dict)
