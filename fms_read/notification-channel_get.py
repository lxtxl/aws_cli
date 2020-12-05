#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-notification-channel.html
if __name__ == '__main__':
    """
	delete-notification-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/delete-notification-channel.html
	put-notification-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/put-notification-channel.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("fms", "get-notification-channel", add_option_dict)