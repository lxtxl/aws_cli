#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/put-room-skill-parameter.html
if __name__ == '__main__':
    """
	delete-room-skill-parameter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-room-skill-parameter.html
	get-room-skill-parameter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-room-skill-parameter.html
    """

    parameter_display_string = """
    # skill-id : The ARN of the skill associated with the room skill parameter. Required.
    # room-skill-parameter : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("alexaforbusiness", "put-room-skill-parameter", "skill-id", "room-skill-parameter", add_option_dict)
