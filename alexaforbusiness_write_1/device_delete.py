#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-device.html
if __name__ == '__main__':
    """
	get-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-device.html
	search-devices : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/search-devices.html
	update-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-device.html
    """

    parameter_display_string = """
    # device-arn : The ARN of the device for which to request details.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("alexaforbusiness", "delete-device", "device-arn", add_option_dict)





