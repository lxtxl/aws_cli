#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-vpn-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-connection.html
	describe-vpn-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpn-connections.html
	modify-vpn-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpn-connection.html
    """

    write_parameter("ec2", "delete-vpn-connection")