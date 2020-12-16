#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-vpc-attachment.html
if __name__ == '__main__':
    """
	accept-transit-gateway-vpc-attachment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/accept-transit-gateway-vpc-attachment.html
	delete-transit-gateway-vpc-attachment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-vpc-attachment.html
	describe-transit-gateway-vpc-attachments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-transit-gateway-vpc-attachments.html
	modify-transit-gateway-vpc-attachment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-transit-gateway-vpc-attachment.html
	reject-transit-gateway-vpc-attachment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reject-transit-gateway-vpc-attachment.html
    """

    parameter_display_string = """
    # transit-gateway-id : The ID of the transit gateway.
    # vpc-id : The ID of the VPC.
    # subnet-ids : The IDs of one or more subnets. You can specify only one subnet per Availability Zone. You must specify at least one subnet, but we recommend that you specify two subnets for better availability. The transit gateway uses one IP address from each specified subnet.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ec2", "create-transit-gateway-vpc-attachment", "transit-gateway-id", "vpc-id", "subnet-ids", add_option_dict)
