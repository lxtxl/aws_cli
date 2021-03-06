#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-cache.html
if __name__ == '__main__':
    """
	add-cache : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/add-cache.html
	refresh-cache : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/refresh-cache.html
	reset-cache : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/reset-cache.html
    """

    parameter_display_string = """
    # gateway-arn : The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("storagegateway", "describe-cache", "gateway-arn", add_option_dict)