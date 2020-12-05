#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	enable-mfa-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/enable-mfa-device.html
	list-mfa-devices : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-mfa-devices.html
	resync-mfa-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/resync-mfa-device.html
    """

    write_parameter("iam", "deactivate-mfa-device")