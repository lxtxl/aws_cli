#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-subnet.html
if __name__ == '__main__':
    """
	delete-subnet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-subnet.html
	describe-subnets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-subnets.html
    """

    parameter_display_string = """
    # cidr-block : The IPv4 network range for the subnet, in CIDR notation. For example, 10.0.0.0/24 . We modify the specified CIDR block to its canonical form; for example, if you specify 100.68.0.18/18 , we modify it to 100.68.0.0/18 .
    # vpc-id : The ID of the VPC.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "create-subnet", "cidr-block", "vpc-id", add_option_dict)
