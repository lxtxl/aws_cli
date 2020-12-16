#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/register-game-server.html
if __name__ == '__main__':
    """
	claim-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/claim-game-server.html
	deregister-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/deregister-game-server.html
	describe-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-game-server.html
	list-game-servers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-game-servers.html
	update-game-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-server.html
    """

    parameter_display_string = """
    # game-server-group-name : A unique identifier for the game server group where the game server is running. Use either the  GameServerGroup name or ARN value.
    # game-server-id : A custom string that uniquely identifies the game server to register. Game server IDs are developer-defined and must be unique across all game server groups in your AWS account.
    # instance-id : The unique identifier for the instance where the game server is running. This ID is available in the instance metadata. EC2 instance IDs use a 17-character format, for example: i-1234567890abcdef0 .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("gamelift", "register-game-server", "game-server-group-name", "game-server-id", "instance-id", add_option_dict)
