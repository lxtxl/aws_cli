#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-channel-message.html
if __name__ == '__main__':
    """
	delete-channel-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-channel-message.html
	list-channel-messages : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-channel-messages.html
	redact-channel-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/redact-channel-message.html
	send-channel-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/send-channel-message.html
	update-channel-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-channel-message.html
    """

    parameter_display_string = """
    # channel-arn : The ARN of the channel.
    # message-id : The ID of the message.
    """

    execute_two_parameter("chime", "get-channel-message", "channel-arn", "message-id", parameter_display_string)