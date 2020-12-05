#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-gateway.html
	describe-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-gateway.html
	list-gateways : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-gateways.html
	update-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-gateway.html
    """

    write_parameter("iotsitewise", "create-gateway")