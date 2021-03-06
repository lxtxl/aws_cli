#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-devices.html
if __name__ == '__main__':
    """
	create-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-device.html
	delete-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-device.html
	update-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-device.html
    """

    parameter_display_string = """
    # global-network-id : The ID of the global network.
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

    execute_one_parameter("networkmanager", "get-devices", "global-network-id", add_option_dict)