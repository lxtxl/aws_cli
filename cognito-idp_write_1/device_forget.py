#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/forget-device.html
if __name__ == '__main__':
    """
	confirm-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/confirm-device.html
	get-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-device.html
	list-devices : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-devices.html
    """

    parameter_display_string = """
    # device-key : The device key.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cognito-idp", "forget-device", "device-key", add_option_dict)





