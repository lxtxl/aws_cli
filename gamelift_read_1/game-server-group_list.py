#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-game-server-group.html
if __name__ == '__main__':
    """
	create-game-server-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-game-server-group.html
	delete-game-server-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-game-server-group.html
	list-game-server-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-game-server-groups.html
	resume-game-server-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/resume-game-server-group.html
	suspend-game-server-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/suspend-game-server-group.html
	update-game-server-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-server-group.html
    """

    parameter_display_string = """
    # game-server-group-name : A unique identifier for the game server group. Use either the  GameServerGroup name or ARN value.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("gamelift", "describe-game-server-group", "game-server-group-name", add_option_dict)