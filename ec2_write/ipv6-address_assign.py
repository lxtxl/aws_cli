#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	unassign-ipv6-addresses : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/unassign-ipv6-addresses.html
    """

    write_parameter("ec2", "assign-ipv6-addresses")