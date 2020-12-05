#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/start-fleet-actions.html
if __name__ == '__main__':
    """
	stop-fleet-actions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/stop-fleet-actions.html
    """

    parameter_display_string = """
    # fleet-id : A unique identifier for a fleet to start actions on. You can use either the fleet ID or ARN value.
    # actions : List of actions to restart on the fleet.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("gamelift", "start-fleet-actions", "fleet-id", "actions", add_option_dict)
