#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-adm-channel.html
if __name__ == '__main__':
    """
	delete-adm-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-adm-channel.html
	update-adm-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-adm-channel.html
    """

    parameter_display_string = """
    # application-id : The unique identifier for the application. This identifier is displayed as the Project ID on the Amazon Pinpoint console.
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

    execute_one_parameter("pinpoint", "get-adm-channel", "application-id", add_option_dict)