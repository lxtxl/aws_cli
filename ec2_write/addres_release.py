#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	allocate-address : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/allocate-address.html
	associate-address : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-address.html
	disassociate-address : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-address.html
    """

    write_parameter("ec2", "release-address")