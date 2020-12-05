#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-vpc-peering-connection.html
if __name__ == '__main__':
    """
	create-vpc-peering-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-vpc-peering-connection.html
	describe-vpc-peering-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-vpc-peering-connections.html
    """

    parameter_display_string = """
    # fleet-id : A unique identifier for a fleet. This fleet specified must match the fleet referenced in the VPC peering connection record. You can use either the fleet ID or ARN value.
    # vpc-peering-connection-id : A unique identifier for a VPC peering connection. This value is included in the  VpcPeeringConnection object, which can be retrieved by calling  DescribeVpcPeeringConnections .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("gamelift", "delete-vpc-peering-connection", "fleet-id", "vpc-peering-connection-id", add_option_dict)
