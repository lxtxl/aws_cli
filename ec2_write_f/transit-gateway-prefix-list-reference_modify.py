#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-transit-gateway-prefix-list-reference : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-prefix-list-reference.html
	delete-transit-gateway-prefix-list-reference : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-prefix-list-reference.html
	get-transit-gateway-prefix-list-references : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-transit-gateway-prefix-list-references.html
    """

    write_parameter("ec2", "modify-transit-gateway-prefix-list-reference")