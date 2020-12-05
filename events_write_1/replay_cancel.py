#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/cancel-replay.html
if __name__ == '__main__':
    """
	describe-replay : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-replay.html
	list-replays : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-replays.html
	start-replay : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/start-replay.html
    """

    parameter_display_string = """
    # replay-name : The name of the replay to cancel.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("events", "cancel-replay", "replay-name", add_option_dict)





