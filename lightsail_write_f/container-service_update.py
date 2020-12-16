#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-container-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-container-service.html
	delete-container-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-container-service.html
	get-container-services : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-container-services.html
    """

    write_parameter("lightsail", "update-container-service")