#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-attribute.html
if __name__ == '__main__':
    """
	modify-vpc-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-attribute.html
    """

    parameter_display_string = """
    # attribute : The VPC attribute.
Possible values:

enableDnsSupport
enableDnsHostnames
    # vpc-id : The ID of the VPC.
    """

    execute_two_parameter("ec2", "describe-vpc-attribute", "attribute", "vpc-id", parameter_display_string)