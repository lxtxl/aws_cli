#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-internet-gateway.html
if __name__ == '__main__':
    """
	create-internet-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-internet-gateway.html
	delete-internet-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-internet-gateway.html
	describe-internet-gateways : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-internet-gateways.html
	detach-internet-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-internet-gateway.html
    """

    parameter_display_string = """
    # internet-gateway-id : The ID of the internet gateway.
    # vpc-id : The ID of the VPC.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "attach-internet-gateway", "internet-gateway-id", "vpc-id", add_option_dict)
