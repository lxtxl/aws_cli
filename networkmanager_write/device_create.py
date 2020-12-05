#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-device.html
	get-devices : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-devices.html
	update-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-device.html
    """

    write_parameter("networkmanager", "create-device")