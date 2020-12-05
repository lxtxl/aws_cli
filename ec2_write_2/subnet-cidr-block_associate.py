#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-subnet-cidr-block.html
if __name__ == '__main__':
    """
	disassociate-subnet-cidr-block : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-subnet-cidr-block.html
    """

    parameter_display_string = """
    # ipv6-cidr-block : The IPv6 CIDR block for your subnet. The subnet must have a /64 prefix length.
    # subnet-id : The ID of your subnet.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "associate-subnet-cidr-block", "ipv6-cidr-block", "subnet-id", add_option_dict)
