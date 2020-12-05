#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-route.html
if __name__ == '__main__':
    """
	create-transit-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-route.html
	export-transit-gateway-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/export-transit-gateway-routes.html
	replace-transit-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-transit-gateway-route.html
	search-transit-gateway-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/search-transit-gateway-routes.html
    """

    parameter_display_string = """
    # transit-gateway-route-table-id : The ID of the transit gateway route table.
    # destination-cidr-block : The CIDR range for the route. This must match the CIDR for the route exactly.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "delete-transit-gateway-route", "transit-gateway-route-table-id", "destination-cidr-block", add_option_dict)
