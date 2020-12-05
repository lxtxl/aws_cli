#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-transit-gateway-prefix-list-references.html
if __name__ == '__main__':
    """
	create-transit-gateway-prefix-list-reference : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-prefix-list-reference.html
	delete-transit-gateway-prefix-list-reference : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-prefix-list-reference.html
	modify-transit-gateway-prefix-list-reference : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-transit-gateway-prefix-list-reference.html
    """

    parameter_display_string = """
    # transit-gateway-route-table-id : The ID of the transit gateway route table.
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

    execute_one_parameter("ec2", "get-transit-gateway-prefix-list-references", "transit-gateway-route-table-id", add_option_dict)