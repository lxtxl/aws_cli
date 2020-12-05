#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-game-servers.html
if __name__ == '__main__':
    """
	claim-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/claim-game-server.html
	deregister-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/deregister-game-server.html
	describe-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-game-server.html
	register-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/register-game-server.html
	update-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-server.html
    """

    parameter_display_string = """
    # game-server-group-name : An identifier for the game server group to retrieve a list of game servers from. Use either the  GameServerGroup name or ARN value.
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

    execute_one_parameter("gamelift", "list-game-servers", "game-server-group-name", add_option_dict)