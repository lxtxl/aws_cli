#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-game-session-placement.html
if __name__ == '__main__':
    """
	start-game-session-placement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/start-game-session-placement.html
	stop-game-session-placement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/stop-game-session-placement.html
    """

    parameter_display_string = """
    # placement-id : A unique identifier for a game session placement to retrieve.
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

    execute_one_parameter("gamelift", "describe-game-session-placement", "placement-id", add_option_dict)