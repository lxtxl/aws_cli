#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-channel.html
if __name__ == '__main__':
    """
	delete-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/delete-channel.html
	describe-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/describe-channel.html
	list-channels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/list-channels.html
	update-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/update-channel.html
    """

    parameter_display_string = """
    # channel-name : The name of the channel.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iotanalytics", "create-channel", "channel-name", add_option_dict)





