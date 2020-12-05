#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-fleet-port-settings.html
if __name__ == '__main__':
    """
	describe-fleet-port-settings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-port-settings.html
    """

    parameter_display_string = """
    # fleet-id : A unique identifier for a fleet to update port settings for. You can use either the fleet ID or ARN value.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("gamelift", "update-fleet-port-settings", "fleet-id", add_option_dict)





