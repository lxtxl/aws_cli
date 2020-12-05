#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/retrieve-tape-archive.html
if __name__ == '__main__':
    """
	delete-tape-archive : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-tape-archive.html
	describe-tape-archives : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-tape-archives.html
    """

    parameter_display_string = """
    # tape-arn : The Amazon Resource Name (ARN) of the virtual tape you want to retrieve from the virtual tape shelf (VTS).
    # gateway-arn : The Amazon Resource Name (ARN) of the gateway you want to retrieve the virtual tape to. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.
You retrieve archived virtual tapes to only one gateway and the gateway must be a tape gateway.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("storagegateway", "retrieve-tape-archive", "tape-arn", "gateway-arn", add_option_dict)
