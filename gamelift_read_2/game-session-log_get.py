#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/get-game-session-log.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # game-session-id : The game session ID
    # save-as : The filename to which the file should be saved (.zip)
    """

    execute_two_parameter("gamelift", "get-game-session-log", "game-session-id", "save-as", parameter_display_string)