#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-egress-only-internet-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-egress-only-internet-gateway.html
	describe-egress-only-internet-gateways : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-egress-only-internet-gateways.html
    """

    write_parameter("ec2", "create-egress-only-internet-gateway")