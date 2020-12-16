#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-channel-message.html
if __name__ == '__main__':
    """
	delete-channel-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-channel-message.html
	get-channel-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-channel-message.html
	list-channel-messages : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-channel-messages.html
	redact-channel-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/redact-channel-message.html
	send-channel-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/send-channel-message.html
    """

    parameter_display_string = """
    # channel-arn : The ARN of the channel.
    # message-id : The ID string of the message being updated.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "update-channel-message", "channel-arn", "message-id", add_option_dict)
