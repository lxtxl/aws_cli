#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-configuration-profiles.html
if __name__ == '__main__':
    """
	create-configuration-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-configuration-profile.html
	delete-configuration-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-configuration-profile.html
	get-configuration-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-configuration-profile.html
	update-configuration-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-configuration-profile.html
    """

    parameter_display_string = """
    # application-id : The application ID.
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

    execute_one_parameter("appconfig", "list-configuration-profiles", "application-id", add_option_dict)