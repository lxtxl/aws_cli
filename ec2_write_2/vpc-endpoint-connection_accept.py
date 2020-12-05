#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/accept-vpc-endpoint-connections.html
if __name__ == '__main__':
    """
	describe-vpc-endpoint-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoint-connections.html
	reject-vpc-endpoint-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reject-vpc-endpoint-connections.html
    """

    parameter_display_string = """
    # service-id : The ID of the VPC endpoint service.
    # vpc-endpoint-ids : The IDs of one or more interface VPC endpoints.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "accept-vpc-endpoint-connections", "service-id", "vpc-endpoint-ids", add_option_dict)
