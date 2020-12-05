#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-local-gateway-route.html
if __name__ == '__main__':
    """
	create-local-gateway-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-local-gateway-route.html
	search-local-gateway-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/search-local-gateway-routes.html
    """

    parameter_display_string = """
    # destination-cidr-block : The CIDR range for the route. This must match the CIDR for the route exactly.
    # local-gateway-route-table-id : The ID of the local gateway route table.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "delete-local-gateway-route", "destination-cidr-block", "local-gateway-route-table-id", add_option_dict)
