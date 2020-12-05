#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-runtime-configuration.html
if __name__ == '__main__':
    """
	describe-runtime-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-runtime-configuration.html
    """

    parameter_display_string = """
    # fleet-id : A unique identifier for a fleet to update runtime configuration for. You can use either the fleet ID or ARN value.
    # runtime-configuration : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("gamelift", "update-runtime-configuration", "fleet-id", "runtime-configuration", add_option_dict)
