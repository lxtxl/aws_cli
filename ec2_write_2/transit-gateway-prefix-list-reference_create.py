#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-prefix-list-reference.html
if __name__ == '__main__':
    """
	delete-transit-gateway-prefix-list-reference : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-prefix-list-reference.html
	get-transit-gateway-prefix-list-references : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-transit-gateway-prefix-list-references.html
	modify-transit-gateway-prefix-list-reference : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-transit-gateway-prefix-list-reference.html
    """

    parameter_display_string = """
    # transit-gateway-route-table-id : The ID of the transit gateway route table.
    # prefix-list-id : The ID of the prefix list that is used for destination matches.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "create-transit-gateway-prefix-list-reference", "transit-gateway-route-table-id", "prefix-list-id", add_option_dict)
