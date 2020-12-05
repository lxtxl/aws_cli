#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-game-server.html
if __name__ == '__main__':
    """
	claim-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/claim-game-server.html
	deregister-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/deregister-game-server.html
	list-game-servers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-game-servers.html
	register-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/register-game-server.html
	update-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-server.html
    """

    parameter_display_string = """
    # game-server-group-name : A unique identifier for the game server group where the game server is running. Use either the  GameServerGroup name or ARN value.
    # game-server-id : A custom string that uniquely identifies the game server information to be retrieved.
    """

    execute_two_parameter("gamelift", "describe-game-server", "game-server-group-name", "game-server-id", parameter_display_string)