#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-container-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-container-image.html
	get-container-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-container-images.html
	push-container-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/push-container-image.html
    """

    write_parameter("lightsail", "register-container-image")