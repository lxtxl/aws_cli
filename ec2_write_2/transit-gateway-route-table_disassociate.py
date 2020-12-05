#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-transit-gateway-route-table.html
if __name__ == '__main__':
    """
	associate-transit-gateway-route-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-transit-gateway-route-table.html
	create-transit-gateway-route-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-route-table.html
	delete-transit-gateway-route-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-route-table.html
	describe-transit-gateway-route-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-transit-gateway-route-tables.html
    """

    parameter_display_string = """
    # transit-gateway-route-table-id : The ID of the transit gateway route table.
    # transit-gateway-attachment-id : The ID of the attachment.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "disassociate-transit-gateway-route-table", "transit-gateway-route-table-id", "transit-gateway-attachment-id", add_option_dict)
