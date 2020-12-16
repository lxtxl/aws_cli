#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-channel-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-channel-message.html
	get-channel-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-channel-message.html
	list-channel-messages : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-channel-messages.html
	send-channel-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/send-channel-message.html
	update-channel-message : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-channel-message.html
    """

    write_parameter("chime", "redact-channel-message")