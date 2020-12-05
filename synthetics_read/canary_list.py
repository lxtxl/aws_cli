#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/describe-canaries.html
if __name__ == '__main__':
    """
	create-canary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/create-canary.html
	delete-canary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/delete-canary.html
	get-canary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/get-canary.html
	start-canary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/start-canary.html
	stop-canary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/stop-canary.html
	update-canary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/update-canary.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("synthetics", "describe-canaries", add_option_dict)