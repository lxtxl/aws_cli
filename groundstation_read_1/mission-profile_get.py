#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/get-mission-profile.html
if __name__ == '__main__':
    """
	create-mission-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/create-mission-profile.html
	delete-mission-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/delete-mission-profile.html
	list-mission-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/list-mission-profiles.html
	update-mission-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/update-mission-profile.html
    """

    parameter_display_string = """
    # mission-profile-id : UUID of a mission profile.
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

    execute_one_parameter("groundstation", "get-mission-profile", "mission-profile-id", add_option_dict)