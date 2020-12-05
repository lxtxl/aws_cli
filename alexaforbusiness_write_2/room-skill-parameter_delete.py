#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-room-skill-parameter.html
if __name__ == '__main__':
    """
	get-room-skill-parameter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-room-skill-parameter.html
	put-room-skill-parameter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/put-room-skill-parameter.html
    """

    parameter_display_string = """
    # skill-id : The ID of the skill from which to remove the room skill parameter details.
    # parameter-key : The room skill parameter key for which to remove details.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("alexaforbusiness", "delete-room-skill-parameter", "skill-id", "parameter-key", add_option_dict)
