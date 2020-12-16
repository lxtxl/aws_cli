#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	activate-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/activate-gateway.html
	delete-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-gateway.html
	disable-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/disable-gateway.html
	list-gateways : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-gateways.html
	shutdown-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/shutdown-gateway.html
    """

    write_parameter("storagegateway", "start-gateway")