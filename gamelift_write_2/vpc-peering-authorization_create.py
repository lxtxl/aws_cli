#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-vpc-peering-authorization.html
if __name__ == '__main__':
    """
	delete-vpc-peering-authorization : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-vpc-peering-authorization.html
	describe-vpc-peering-authorizations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-vpc-peering-authorizations.html
    """

    parameter_display_string = """
    # game-lift-aws-account-id : A unique identifier for the AWS account that you use to manage your Amazon GameLift fleet. You can find your Account ID in the AWS Management Console under account settings.
    # peer-vpc-id : A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region where your fleet is deployed. Look up a VPC ID using the VPC Dashboard in the AWS Management Console. Learn more about VPC peering in VPC Peering with Amazon GameLift Fleets .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("gamelift", "create-vpc-peering-authorization", "game-lift-aws-account-id", "peer-vpc-id", add_option_dict)
