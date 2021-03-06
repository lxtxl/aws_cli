#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	accept-handshake : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/accept-handshake.html
	decline-handshake : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/decline-handshake.html
	describe-handshake : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-handshake.html
    """

    write_parameter("organizations", "cancel-handshake")