#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-player-session.html
if __name__ == '__main__':
    """
	create-player-sessions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-player-sessions.html
	describe-player-sessions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-player-sessions.html
    """

    parameter_display_string = """
    # game-session-id : A unique identifier for the game session to add a player to.
    # player-id : A unique identifier for a player. Player IDs are developer-defined.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("gamelift", "create-player-session", "game-session-id", "player-id", add_option_dict)
