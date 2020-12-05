#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-classic-link-vpc.html
if __name__ == '__main__':
    """
	attach-classic-link-vpc : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-classic-link-vpc.html
    """

    parameter_display_string = """
    # instance-id : The ID of the instance to unlink from the VPC.
    # vpc-id : The ID of the VPC to which the instance is linked.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "detach-classic-link-vpc", "instance-id", "vpc-id", add_option_dict)
