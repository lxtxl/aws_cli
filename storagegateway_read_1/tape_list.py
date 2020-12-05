#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-tapes.html
if __name__ == '__main__':
    """
	create-tapes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-tapes.html
	delete-tape : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-tape.html
	list-tapes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-tapes.html
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

    execute_one_parameter("storagegateway", "describe-tapes", "gateway-arn", add_option_dict)