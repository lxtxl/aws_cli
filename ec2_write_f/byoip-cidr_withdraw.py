#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	advertise-byoip-cidr : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/advertise-byoip-cidr.html
	deprovision-byoip-cidr : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/deprovision-byoip-cidr.html
	describe-byoip-cidrs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-byoip-cidrs.html
	provision-byoip-cidr : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/provision-byoip-cidr.html
    """

    write_parameter("ec2", "withdraw-byoip-cidr")