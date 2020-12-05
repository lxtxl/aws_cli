#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	attach-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/attach-disk.html
	create-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-disk.html
	detach-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/detach-disk.html
	get-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-disk.html
	get-disks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-disks.html
    """

    write_parameter("lightsail", "delete-disk")