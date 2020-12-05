#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-network-profile.html
if __name__ == '__main__':
    """
	create-network-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-network-profile.html
	delete-network-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-network-profile.html
	search-network-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/search-network-profiles.html
	update-network-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-network-profile.html
    """

    parameter_display_string = """
    # network-profile-arn : The ARN of the network profile associated with a device.
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

    execute_one_parameter("alexaforbusiness", "get-network-profile", "network-profile-arn", add_option_dict)