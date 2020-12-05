#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-fleet.html
if __name__ == '__main__':
    """
	create-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-fleet.html
	list-fleets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-fleets.html
    """

    parameter_display_string = """
    # fleet-id : A unique identifier for a fleet to be deleted. You can use either the fleet ID or ARN value.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("gamelift", "delete-fleet", "fleet-id", add_option_dict)





