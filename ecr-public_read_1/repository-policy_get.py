#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/get-repository-policy.html
if __name__ == '__main__':
    """
	delete-repository-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/delete-repository-policy.html
	set-repository-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/set-repository-policy.html
    """

    parameter_display_string = """
    # repository-name : The name of the repository with the policy to retrieve.
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

    execute_one_parameter("ecr-public", "get-repository-policy", "repository-name", add_option_dict)