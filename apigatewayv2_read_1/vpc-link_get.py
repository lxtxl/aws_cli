#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-vpc-link.html
if __name__ == '__main__':
    """
	create-vpc-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-vpc-link.html
	delete-vpc-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-vpc-link.html
	get-vpc-links : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-vpc-links.html
	update-vpc-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-vpc-link.html
    """

    parameter_display_string = """
    # vpc-link-id : The ID of the VPC link.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("apigatewayv2", "get-vpc-link", "vpc-link-id", add_option_dict)