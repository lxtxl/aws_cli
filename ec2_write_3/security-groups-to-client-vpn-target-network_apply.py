#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/apply-security-groups-to-client-vpn-target-network.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # client-vpn-endpoint-id : The ID of the Client VPN endpoint.
    # vpc-id : The ID of the VPC in which the associated target network is located.
    # security-group-ids : The IDs of the security groups to apply to the associated target network. Up to 5 security groups can be applied to an associated target network.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ec2", "apply-security-groups-to-client-vpn-target-network", "client-vpn-endpoint-id", "vpc-id", "security-group-ids", add_option_dict)
