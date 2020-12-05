#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-device.html
if __name__ == '__main__':
    """
	create-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-device.html
	get-devices : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-devices.html
	update-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-device.html
    """

    parameter_display_string = """
    # global-network-id : The ID of the global network.
    # device-id : The ID of the device.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("networkmanager", "delete-device", "global-network-id", "device-id", add_option_dict)
