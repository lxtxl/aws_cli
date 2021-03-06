#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/set-smb-guest-password.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # gateway-arn : The Amazon Resource Name (ARN) of the file gateway the SMB file share is associated with.
    # password : The password that you want to set for your SMB server.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("storagegateway", "set-smb-guest-password", "gateway-arn", "password", add_option_dict)
