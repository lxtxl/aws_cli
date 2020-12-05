#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-game-session.html
if __name__ == '__main__':
    """
	describe-game-sessions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-game-sessions.html
	search-game-sessions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/search-game-sessions.html
	update-game-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-session.html
    """

    parameter_display_string = """
    # maximum-player-session-count : The maximum number of players that can be connected simultaneously to the game session.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("gamelift", "create-game-session", "maximum-player-session-count", add_option_dict)





