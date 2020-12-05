#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-dhcp-options.html
if __name__ == '__main__':
    """
	create-dhcp-options : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-dhcp-options.html
	delete-dhcp-options : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-dhcp-options.html
	describe-dhcp-options : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-dhcp-options.html
    """

    parameter_display_string = """
    # dhcp-options-id : The ID of the DHCP options set, or default to associate no DHCP options with the VPC.
    # vpc-id : The ID of the VPC.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "associate-dhcp-options", "dhcp-options-id", "vpc-id", add_option_dict)
