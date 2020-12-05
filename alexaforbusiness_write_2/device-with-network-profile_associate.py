#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/associate-device-with-network-profile.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # device-arn : The device ARN.
    # network-profile-arn : The ARN of the network profile to associate with a device.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("alexaforbusiness", "associate-device-with-network-profile", "device-arn", "network-profile-arn", add_option_dict)
