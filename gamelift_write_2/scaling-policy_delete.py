#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-scaling-policy.html
if __name__ == '__main__':
    """
	describe-scaling-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-scaling-policies.html
	put-scaling-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/put-scaling-policy.html
    """

    parameter_display_string = """
    # name : A descriptive label that is associated with a scaling policy. Policy names do not need to be unique.
    # fleet-id : A unique identifier for a fleet to be deleted. You can use either the fleet ID or ARN value.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("gamelift", "delete-scaling-policy", "name", "fleet-id", add_option_dict)
