#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/accept-match.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # ticket-id : A unique identifier for a matchmaking ticket. The ticket must be in status REQUIRES_ACCEPTANCE ; otherwise this request will fail.
    # player-ids : A unique identifier for a player delivering the response. This parameter can include one or multiple player IDs.
(string)
    # acceptance-type : Player response to the proposed match.
Possible values:

ACCEPT
REJECT
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("gamelift", "accept-match", "ticket-id", "player-ids", "acceptance-type", add_option_dict)
