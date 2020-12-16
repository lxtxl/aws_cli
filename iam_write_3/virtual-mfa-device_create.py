#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-virtual-mfa-device.html
if __name__ == '__main__':
    """
	delete-virtual-mfa-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-virtual-mfa-device.html
	list-virtual-mfa-devices : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-virtual-mfa-devices.html
    """

    parameter_display_string = """
    # virtual-mfa-device-name : The name of the virtual MFA device. Use with path to uniquely identify a virtual MFA device.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    # outfile : The output path and file name where the bootstrap information will be stored.
    # bootstrap-method : Method to use to seed the virtual MFA. Valid values are: QRCodePNG | Base32StringSeed
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("iam", "create-virtual-mfa-device", "virtual-mfa-device-name", "outfile", "bootstrap-method", add_option_dict)
