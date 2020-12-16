#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/validate-configuration.html
if __name__ == '__main__':
    """
	get-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-configuration.html
    """

    parameter_display_string = """
    # application-id : The application ID.
    # configuration-profile-id : The configuration profile ID.
    # configuration-version : The version of the configuration to validate.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("appconfig", "validate-configuration", "application-id", "configuration-profile-id", "configuration-version", add_option_dict)
