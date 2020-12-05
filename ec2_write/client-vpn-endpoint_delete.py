#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-client-vpn-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-client-vpn-endpoint.html
	describe-client-vpn-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-client-vpn-endpoints.html
	modify-client-vpn-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-client-vpn-endpoint.html
    """

    write_parameter("ec2", "delete-client-vpn-endpoint")