#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/unassign-private-ip-addresses.html
if __name__ == '__main__':
    """
	assign-private-ip-addresses : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/assign-private-ip-addresses.html
    """

    parameter_display_string = """
    # network-interface-id : The ID of the network interface.
    # private-ip-addresses : The secondary private IP addresses to unassign from the network interface. You can specify this option multiple times to unassign more than one IP address.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "unassign-private-ip-addresses", "network-interface-id", "private-ip-addresses", add_option_dict)
