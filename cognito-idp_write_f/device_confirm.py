#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	forget-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/forget-device.html
	get-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-device.html
	list-devices : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-devices.html
    """

    write_parameter("cognito-idp", "confirm-device")