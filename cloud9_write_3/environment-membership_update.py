#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/update-environment-membership.html
if __name__ == '__main__':
    """
	create-environment-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/create-environment-membership.html
	delete-environment-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/delete-environment-membership.html
	describe-environment-memberships : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/describe-environment-memberships.html
    """

    parameter_display_string = """
    # environment-id : The ID of the environment for the environment member whose settings you want to change.
    # user-arn : The Amazon Resource Name (ARN) of the environment member whose settings you want to change.
    # permissions : The replacement type of environment member permissions you want to associate with this environment member. Available values include:

read-only : Has read-only access to the environment.
read-write : Has read-write access to the environment.

Possible values:

read-write
read-only
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cloud9", "update-environment-membership", "environment-id", "user-arn", "permissions", add_option_dict)
