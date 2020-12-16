#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-channels.html
if __name__ == '__main__':
    """
	create-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/create-channel.html
	delete-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-channel.html
	describe-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-channel.html
	start-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/start-channel.html
	stop-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/stop-channel.html
	update-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-channel.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("medialive", "list-channels", add_option_dict)