#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-realtime-log-config.html
if __name__ == '__main__':
    """
	create-realtime-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-realtime-log-config.html
	delete-realtime-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-realtime-log-config.html
	list-realtime-log-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-realtime-log-configs.html
	update-realtime-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-realtime-log-config.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("cloudfront", "get-realtime-log-config", add_option_dict)