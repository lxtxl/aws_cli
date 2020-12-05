#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-matchmaking-configuration.html
if __name__ == '__main__':
    """
	create-matchmaking-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-matchmaking-configuration.html
	delete-matchmaking-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-matchmaking-configuration.html
	describe-matchmaking-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-matchmaking-configurations.html
    """

    parameter_display_string = """
    # name : A unique identifier for a matchmaking configuration to update. You can use either the configuration name or ARN value.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("gamelift", "update-matchmaking-configuration", "name", add_option_dict)





