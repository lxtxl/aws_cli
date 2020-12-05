#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/create-channel.html
	delete-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/delete-channel.html
	describe-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/describe-channel.html
	list-channels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/list-channels.html
    """

    write_parameter("mediapackage", "update-channel")