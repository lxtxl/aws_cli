#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/describe-channel.html
if __name__ == '__main__':
    """
	create-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-channel.html
	delete-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/delete-channel.html
	list-channels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/list-channels.html
	update-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/update-channel.html
    """

    parameter_display_string = """
    # channel-name : The name of the channel whose information is retrieved.
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

    execute_one_parameter("iotanalytics", "describe-channel", "channel-name", add_option_dict)