#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-vpc-link.html
if __name__ == '__main__':
    """
	create-vpc-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-vpc-link.html
	delete-vpc-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-vpc-link.html
	get-vpc-links : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-vpc-links.html
	update-vpc-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-vpc-link.html
    """

    parameter_display_string = """
    # vpc-link-id : [Required] The identifier of the  VpcLink . It is used in an  Integration to reference this  VpcLink .
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

    execute_one_parameter("apigateway", "get-vpc-link", "vpc-link-id", add_option_dict)