#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/reset-cache.html
if __name__ == '__main__':
    """
	add-cache : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/add-cache.html
	describe-cache : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-cache.html
	refresh-cache : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/refresh-cache.html
    """

    parameter_display_string = """
    # gateway-arn : The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("storagegateway", "reset-cache", "gateway-arn", add_option_dict)





