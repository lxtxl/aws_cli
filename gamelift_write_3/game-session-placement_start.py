#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/start-game-session-placement.html
if __name__ == '__main__':
    """
	describe-game-session-placement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-game-session-placement.html
	stop-game-session-placement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/stop-game-session-placement.html
    """

    parameter_display_string = """
    # placement-id : A unique identifier to assign to the new game session placement. This value is developer-defined. The value must be unique across all Regions and cannot be reused unless you are resubmitting a canceled or timed-out placement request.
    # game-session-queue-name : Name of the queue to use to place the new game session. You can use either the queue name or ARN value.
    # maximum-player-session-count : The maximum number of players that can be connected simultaneously to the game session.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("gamelift", "start-game-session-placement", "placement-id", "game-session-queue-name", "maximum-player-session-count", add_option_dict)
