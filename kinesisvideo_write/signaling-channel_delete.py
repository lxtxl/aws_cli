#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-signaling-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/create-signaling-channel.html
	describe-signaling-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/describe-signaling-channel.html
	list-signaling-channels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/list-signaling-channels.html
	update-signaling-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/update-signaling-channel.html
    """

    write_parameter("kinesisvideo", "delete-signaling-channel")