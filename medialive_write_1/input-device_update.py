#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-input-device.html
if __name__ == '__main__':
    """
	describe-input-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-input-device.html
	list-input-devices : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-input-devices.html
	transfer-input-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/transfer-input-device.html
    """

    parameter_display_string = """
    # input-device-id : The unique ID of the input device. For example, hd-123456789abcdef.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("medialive", "update-input-device", "input-device-id", add_option_dict)





