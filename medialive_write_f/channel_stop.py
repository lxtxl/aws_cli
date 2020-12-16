#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/create-channel.html
	delete-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-channel.html
	describe-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-channel.html
	list-channels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-channels.html
	start-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/start-channel.html
	update-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-channel.html
    """

    write_parameter("medialive", "stop-channel")