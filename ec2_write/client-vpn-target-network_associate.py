#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-client-vpn-target-networks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-client-vpn-target-networks.html
	disassociate-client-vpn-target-network : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-client-vpn-target-network.html
    """

    write_parameter("ec2", "associate-client-vpn-target-network")