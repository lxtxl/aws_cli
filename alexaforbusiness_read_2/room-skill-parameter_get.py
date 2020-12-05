#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-room-skill-parameter.html
if __name__ == '__main__':
    """
	delete-room-skill-parameter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-room-skill-parameter.html
	put-room-skill-parameter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/put-room-skill-parameter.html
    """

    parameter_display_string = """
    # skill-id : The ARN of the skill from which to get the room skill parameter details. Required.
    # parameter-key : The room skill parameter key for which to get details. Required.
    """

    execute_two_parameter("alexaforbusiness", "get-room-skill-parameter", "skill-id", "parameter-key", parameter_display_string)