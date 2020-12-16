#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-matchmaking-configurations.html
if __name__ == '__main__':
    """
	create-matchmaking-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-matchmaking-configuration.html
	delete-matchmaking-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-matchmaking-configuration.html
	update-matchmaking-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-matchmaking-configuration.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("gamelift", "describe-matchmaking-configurations", add_option_dict)