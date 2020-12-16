#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-apns-sandbox-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-apns-sandbox-channel.html
	get-apns-sandbox-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-apns-sandbox-channel.html
    """

    write_parameter("pinpoint", "update-apns-sandbox-channel")