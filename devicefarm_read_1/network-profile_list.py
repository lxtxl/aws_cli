#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-network-profiles.html
if __name__ == '__main__':
    """
	create-network-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-network-profile.html
	delete-network-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-network-profile.html
	get-network-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-network-profile.html
	update-network-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-network-profile.html
    """

    parameter_display_string = """
    # arn : The Amazon Resource Name (ARN) of the project for which you want to list network profiles.
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

    execute_one_parameter("devicefarm", "list-network-profiles", "arn", add_option_dict)