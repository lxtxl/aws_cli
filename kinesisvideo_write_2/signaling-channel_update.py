#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/update-signaling-channel.html
if __name__ == '__main__':
    """
	create-signaling-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/create-signaling-channel.html
	delete-signaling-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/delete-signaling-channel.html
	describe-signaling-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/describe-signaling-channel.html
	list-signaling-channels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/list-signaling-channels.html
    """

    parameter_display_string = """
    # channel-arn : The Amazon Resource Name (ARN) of the signaling channel that you want to update.
    # current-version : The current version of the signaling channel that you want to update.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kinesisvideo", "update-signaling-channel", "channel-arn", "current-version", add_option_dict)
