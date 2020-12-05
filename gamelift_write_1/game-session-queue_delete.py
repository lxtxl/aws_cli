#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-game-session-queue.html
if __name__ == '__main__':
    """
	create-game-session-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-game-session-queue.html
	describe-game-session-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-game-session-queues.html
	update-game-session-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-session-queue.html
    """

    parameter_display_string = """
    # name : A descriptive label that is associated with game session queue. Queue names must be unique within each Region. You can use either the queue ID or ARN value.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("gamelift", "delete-game-session-queue", "name", add_option_dict)





