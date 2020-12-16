#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-channel.html
if __name__ == '__main__':
    """
	delete-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-channel.html
	describe-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-channel.html
	list-channels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-channels.html
	update-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-channel.html
    """

    parameter_display_string = """
    # app-instance-arn : The ARN of the channel request.
    # name : The name of the channel.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "create-channel", "app-instance-arn", "name", add_option_dict)
