#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-transit-gateway-route-table-propagations.html
if __name__ == '__main__':
    """
	disable-transit-gateway-route-table-propagation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-transit-gateway-route-table-propagation.html
	enable-transit-gateway-route-table-propagation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-transit-gateway-route-table-propagation.html
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

    execute_one_parameter("ec2", "get-transit-gateway-route-table-propagations", "transit-gateway-route-table-id", add_option_dict)