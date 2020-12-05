#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-configuration-profile.html
if __name__ == '__main__':
    """
	create-configuration-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-configuration-profile.html
	get-configuration-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-configuration-profile.html
	list-configuration-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-configuration-profiles.html
	update-configuration-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-configuration-profile.html
    """

    parameter_display_string = """
    # application-id : The application ID that includes the configuration profile you want to delete.
    # configuration-profile-id : The ID of the configuration profile you want to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("appconfig", "delete-configuration-profile", "application-id", "configuration-profile-id", add_option_dict)
