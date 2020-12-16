#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/disassociate-link.html
if __name__ == '__main__':
    """
	associate-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/associate-link.html
	create-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-link.html
	delete-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-link.html
	get-links : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-links.html
	update-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-link.html
    """

    parameter_display_string = """
    # global-network-id : The ID of the global network.
    # device-id : The ID of the device.
    # link-id : The ID of the link.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("networkmanager", "disassociate-link", "global-network-id", "device-id", "link-id", add_option_dict)
