#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/describe-signaling-channel.html
if __name__ == '__main__':
    """
	create-signaling-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/create-signaling-channel.html
	delete-signaling-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/delete-signaling-channel.html
	list-signaling-channels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/list-signaling-channels.html
	update-signaling-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/update-signaling-channel.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("kinesisvideo", "describe-signaling-channel", add_option_dict)