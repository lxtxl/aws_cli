#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-ota-update.html
if __name__ == '__main__':
    """
	create-ota-update : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-ota-update.html
	delete-ota-update : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-ota-update.html
	list-ota-updates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-ota-updates.html
    """

    parameter_display_string = """
    # ota-update-id : The OTA update ID.
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

    execute_one_parameter("iot", "get-ota-update", "ota-update-id", add_option_dict)