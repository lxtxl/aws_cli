#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-transit-gateway-route.html
if __name__ == '__main__':
    """
	create-transit-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-route.html
	delete-transit-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-route.html
	export-transit-gateway-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/export-transit-gateway-routes.html
	search-transit-gateway-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/search-transit-gateway-routes.html
    """

    parameter_display_string = """
    # destination-cidr-block : The CIDR range used for the destination match. Routing decisions are based on the most specific match.
    # transit-gateway-route-table-id : The ID of the route table.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "replace-transit-gateway-route", "destination-cidr-block", "transit-gateway-route-table-id", add_option_dict)
