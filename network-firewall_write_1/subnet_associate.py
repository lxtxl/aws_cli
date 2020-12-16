#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/associate-subnets.html
if __name__ == '__main__':
    """
	disassociate-subnets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/disassociate-subnets.html
    """

    parameter_display_string = """
    # subnet-mappings : The IDs of the subnets that you want to associate with the firewall.
(structure)

The ID for a subnet that you want to associate with the firewall. This is used with  CreateFirewall and  AssociateSubnets . AWS Network Firewall creates an instance of the associated firewall in each subnet that you specify, to filter traffic in the subnetâs Availability Zone.
SubnetId -> (string)

The unique identifier for the subnet.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("network-firewall", "associate-subnets", "subnet-mappings", add_option_dict)





