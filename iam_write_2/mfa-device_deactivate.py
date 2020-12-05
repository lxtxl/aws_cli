#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/deactivate-mfa-device.html
if __name__ == '__main__':
    """
	enable-mfa-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/enable-mfa-device.html
	list-mfa-devices : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-mfa-devices.html
	resync-mfa-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/resync-mfa-device.html
    """

    parameter_display_string = """
    # user-name : The name of the user whose MFA device you want to deactivate.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    # serial-number : The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the device ARN.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@:/-
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "deactivate-mfa-device", "user-name", "serial-number", add_option_dict)
