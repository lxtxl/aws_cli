#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	attach-vpn-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-vpn-gateway.html
	create-vpn-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-gateway.html
	delete-vpn-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpn-gateway.html
	describe-vpn-gateways : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpn-gateways.html
    """

    write_parameter("ec2", "detach-vpn-gateway")