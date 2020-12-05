#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/stop-matchmaking.html
if __name__ == '__main__':
    """
	describe-matchmaking : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-matchmaking.html
	start-matchmaking : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/start-matchmaking.html
    """

    parameter_display_string = """
    # ticket-id : A unique identifier for a matchmaking ticket.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("gamelift", "stop-matchmaking", "ticket-id", add_option_dict)





