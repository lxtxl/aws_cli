#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-vpc-link.html
if __name__ == '__main__':
    """
	delete-vpc-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-vpc-link.html
	get-vpc-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-vpc-link.html
	get-vpc-links : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-vpc-links.html
	update-vpc-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-vpc-link.html
    """

    parameter_display_string = """
    # name : The name of the VPC link.
    # subnet-ids : A list of subnet IDs to include in the VPC link.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigatewayv2", "create-vpc-link", "name", "subnet-ids", add_option_dict)
