#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/claim-game-server.html
if __name__ == '__main__':
    """
	deregister-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/deregister-game-server.html
	describe-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-game-server.html
	list-game-servers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-game-servers.html
	register-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/register-game-server.html
	update-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-server.html
    """

    parameter_display_string = """
    # game-server-group-name : A unique identifier for the game server group where the game server is running. Use either the  GameServerGroup name or ARN value.. If you are not specifying a game server to claim, this value identifies where you want GameLift FleetIQ to look for an available game server to claim.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("gamelift", "claim-game-server", "game-server-group-name", add_option_dict)





