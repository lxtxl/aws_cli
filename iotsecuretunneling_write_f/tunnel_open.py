#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	close-tunnel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/close-tunnel.html
	describe-tunnel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/describe-tunnel.html
	list-tunnels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/list-tunnels.html
    """

    write_parameter("iotsecuretunneling", "open-tunnel")