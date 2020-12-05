#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/list-flows.html
if __name__ == '__main__':
    """
	create-flow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/create-flow.html
	delete-flow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/delete-flow.html
	describe-flow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/describe-flow.html
	start-flow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/start-flow.html
	stop-flow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/stop-flow.html
	update-flow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/update-flow.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("mediaconnect", "list-flows", add_option_dict)