#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-input-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-input-device.html
	list-input-devices : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-input-devices.html
	update-input-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-input-device.html
    """

    write_parameter("medialive", "transfer-input-device")