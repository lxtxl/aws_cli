#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-vpc-peering-connection.html
if __name__ == '__main__':
    """
	delete-vpc-peering-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-vpc-peering-connection.html
	describe-vpc-peering-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-vpc-peering-connections.html
    """

    parameter_display_string = """
    # fleet-id : A unique identifier for a fleet. You can use either the fleet ID or ARN value. This tells Amazon GameLift which GameLift VPC to peer with.
    # peer-vpc-aws-account-id : A unique identifier for the AWS account with the VPC that you want to peer your Amazon GameLift fleet with. You can find your Account ID in the AWS Management Console under account settings.
    # peer-vpc-id : A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region where your fleet is deployed. Look up a VPC ID using the VPC Dashboard in the AWS Management Console. Learn more about VPC peering in VPC Peering with Amazon GameLift Fleets .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("gamelift", "create-vpc-peering-connection", "fleet-id", "peer-vpc-aws-account-id", "peer-vpc-id", add_option_dict)
