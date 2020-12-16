#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-network-profile.html
if __name__ == '__main__':
    """
	delete-network-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-network-profile.html
	get-network-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-network-profile.html
	search-network-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/search-network-profiles.html
	update-network-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-network-profile.html
    """

    parameter_display_string = """
    # network-profile-name : The name of the network profile associated with a device.
    # ssid : The SSID of the Wi-Fi network.
    # security-type : The security type of the Wi-Fi network. This can be WPA2_ENTERPRISE, WPA2_PSK, WPA_PSK, WEP, or OPEN.
Possible values:

OPEN
WEP
WPA_PSK
WPA2_PSK
WPA2_ENTERPRISE
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("alexaforbusiness", "create-network-profile", "network-profile-name", "ssid", "security-type", add_option_dict)
