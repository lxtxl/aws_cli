#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-availability-monitor-test.html
if __name__ == '__main__':
    """
	start-availability-monitor-test : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/start-availability-monitor-test.html
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

    execute_one_parameter("storagegateway", "describe-availability-monitor-test", "gateway-arn", add_option_dict)