#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-fleet.html
if __name__ == '__main__':
    """
	create-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-fleet.html
	delete-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/delete-fleet.html
	list-fleets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-fleets.html
    """

    parameter_display_string = """
    # fleet : The Amazon Resource Name (ARN) of the fleet.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("robomaker", "describe-fleet", "fleet", add_option_dict)