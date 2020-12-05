#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint.html
if __name__ == '__main__':
    """
	delete-vpc-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpc-endpoints.html
	describe-vpc-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoints.html
	modify-vpc-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-endpoint.html
    """

    parameter_display_string = """
    # vpc-id : The ID of the VPC in which the endpoint will be used.
    # service-name : The service name. To get a list of available services, use the  DescribeVpcEndpointServices request, or get the name from the service provider.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "create-vpc-endpoint", "vpc-id", "service-name", add_option_dict)
