#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-security-profile.html
if __name__ == '__main__':
    """
	attach-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-security-profile.html
	create-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-security-profile.html
	delete-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-security-profile.html
	detach-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/detach-security-profile.html
	list-security-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-security-profiles.html
	update-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-security-profile.html
    """

    parameter_display_string = """
    # security-profile-name : The name of the security profile whose information you want to get.
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

    execute_one_parameter("iot", "describe-security-profile", "security-profile-name", add_option_dict)