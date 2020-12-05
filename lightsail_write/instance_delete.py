#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-instances.html
	get-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instance.html
	get-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instances.html
	reboot-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/reboot-instance.html
	start-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/start-instance.html
	stop-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/stop-instance.html
    """

    write_parameter("lightsail", "delete-instance")