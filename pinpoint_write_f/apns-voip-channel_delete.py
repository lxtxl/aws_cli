#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-apns-voip-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-apns-voip-channel.html
	update-apns-voip-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-apns-voip-channel.html
    """

    write_parameter("pinpoint", "delete-apns-voip-channel")