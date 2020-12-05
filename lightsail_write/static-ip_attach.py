#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	allocate-static-ip : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/allocate-static-ip.html
	detach-static-ip : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/detach-static-ip.html
	get-static-ip : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-static-ip.html
	get-static-ips : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-static-ips.html
	release-static-ip : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/release-static-ip.html
    """

    write_parameter("lightsail", "attach-static-ip")