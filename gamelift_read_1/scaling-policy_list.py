#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-scaling-policies.html
if __name__ == '__main__':
    """
	delete-scaling-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-scaling-policy.html
	put-scaling-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/put-scaling-policy.html
    """

    parameter_display_string = """
    # fleet-id : A unique identifier for a fleet to retrieve scaling policies for. You can use either the fleet ID or ARN value.
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

    execute_one_parameter("gamelift", "describe-scaling-policies", "fleet-id", add_option_dict)