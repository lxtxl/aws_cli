#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-virtual-mfa-device.html
if __name__ == '__main__':
    """
	create-virtual-mfa-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-virtual-mfa-device.html
	list-virtual-mfa-devices : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-virtual-mfa-devices.html
    """

    parameter_display_string = """
    # serial-number : The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the same as the ARN.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@:/-
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "delete-virtual-mfa-device", "serial-number", add_option_dict)





