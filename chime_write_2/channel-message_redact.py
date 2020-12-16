#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/redact-channel-message.html
if __name__ == '__main__':
    """
	delete-channel-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-channel-message.html
	get-channel-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-channel-message.html
	list-channel-messages : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-channel-messages.html
	send-channel-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/send-channel-message.html
	update-channel-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-channel-message.html
    """

    parameter_display_string = """
    # channel-arn : The ARN of the channel containing the messages that you want to redact.
    # message-id : The ID of the message being redacted.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "redact-channel-message", "channel-arn", "message-id", add_option_dict)
