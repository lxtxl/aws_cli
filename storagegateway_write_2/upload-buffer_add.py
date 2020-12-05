#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/add-upload-buffer.html
if __name__ == '__main__':
    """
	describe-upload-buffer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-upload-buffer.html
    """

    parameter_display_string = """
    # gateway-arn : The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.
    # disk-ids : An array of strings that identify disks that are to be configured as working storage. Each string has a minimum length of 1 and maximum length of 300. You can get the disk IDs from the  ListLocalDisks API.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("storagegateway", "add-upload-buffer", "gateway-arn", "disk-ids", add_option_dict)
