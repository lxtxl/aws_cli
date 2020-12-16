#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-channel.html
if __name__ == '__main__':
    """
	create-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-channel.html
	delete-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-channel.html
	describe-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-channel.html
	list-channels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-channels.html
    """

    parameter_display_string = """
    # channel-arn : The ARN of the channel.
    # name : The name of the channel.
    # mode : The mode of the update request.
Possible values:

UNRESTRICTED
RESTRICTED
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("chime", "update-channel", "channel-arn", "name", "mode", add_option_dict)
