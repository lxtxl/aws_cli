#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/unassign-ipv6-addresses.html
if __name__ == '__main__':
    """
	assign-ipv6-addresses : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/assign-ipv6-addresses.html
    """

    parameter_display_string = """
    # ipv6-addresses : The IPv6 addresses to unassign from the network interface.
(string)
    # network-interface-id : The ID of the network interface.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "unassign-ipv6-addresses", "ipv6-addresses", "network-interface-id", add_option_dict)
