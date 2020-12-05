#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	attach-internet-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-internet-gateway.html
	create-internet-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-internet-gateway.html
	delete-internet-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-internet-gateway.html
	describe-internet-gateways : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-internet-gateways.html
    """

    write_parameter("ec2", "detach-internet-gateway")