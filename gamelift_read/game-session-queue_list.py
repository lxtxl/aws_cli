#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-game-session-queues.html
if __name__ == '__main__':
    """
	create-game-session-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-game-session-queue.html
	delete-game-session-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-game-session-queue.html
	update-game-session-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-session-queue.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("gamelift", "describe-game-session-queues", add_option_dict)