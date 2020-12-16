#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-classic-link-vpc.html
if __name__ == '__main__':
    """
	detach-classic-link-vpc : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-classic-link-vpc.html
    """

    parameter_display_string = """
    # groups : The ID of one or more of the VPCâs security groups. You cannot specify security groups from a different VPC.
(string)
    # instance-id : The ID of an EC2-Classic instance to link to the ClassicLink-enabled VPC.
    # vpc-id : The ID of a ClassicLink-enabled VPC.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ec2", "attach-classic-link-vpc", "groups", "instance-id", "vpc-id", add_option_dict)
