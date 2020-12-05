#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-gateways.html
if __name__ == '__main__':
    """
	activate-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/activate-gateway.html
	delete-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-gateway.html
	disable-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/disable-gateway.html
	shutdown-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/shutdown-gateway.html
	start-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/start-gateway.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("storagegateway", "list-gateways", add_option_dict)