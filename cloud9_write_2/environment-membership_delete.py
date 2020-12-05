#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/delete-environment-membership.html
if __name__ == '__main__':
    """
	create-environment-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/create-environment-membership.html
	describe-environment-memberships : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/describe-environment-memberships.html
	update-environment-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/update-environment-membership.html
    """

    parameter_display_string = """
    # environment-id : The ID of the environment to delete the environment member from.
    # user-arn : The Amazon Resource Name (ARN) of the environment member to delete from the environment.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloud9", "delete-environment-membership", "environment-id", "user-arn", add_option_dict)
