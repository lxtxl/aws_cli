#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-transit-gateway-route-table-propagation.html
if __name__ == '__main__':
    """
	enable-transit-gateway-route-table-propagation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-transit-gateway-route-table-propagation.html
	get-transit-gateway-route-table-propagations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-transit-gateway-route-table-propagations.html
    """

    parameter_display_string = """
    # transit-gateway-route-table-id : The ID of the propagation route table.
    # transit-gateway-attachment-id : The ID of the attachment.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "disable-transit-gateway-route-table-propagation", "transit-gateway-route-table-id", "transit-gateway-attachment-id", add_option_dict)
