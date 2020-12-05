#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/describe-environments.html
if __name__ == '__main__':
    """
	delete-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/delete-environment.html
	list-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/list-environments.html
	update-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/update-environment.html
    """

    parameter_display_string = """
    # environment-ids : The IDs of individual environments to get information about.
(string)
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

    execute_one_parameter("cloud9", "describe-environments", "environment-ids", add_option_dict)